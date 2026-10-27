// DOM integration test: real event delegation, rendered options, feedback,
// navigation, completion, mistake review and localStorage round-trip.
const { JSDOM, VirtualConsole } = require('jsdom');
const { readFileSync } = require('node:fs');
const assert = require('node:assert/strict');
const errors = [];
const vc = new VirtualConsole();
vc.on('jsdomError', e => errors.push(e));
const html = readFileSync('obg-mastery-path.html', 'utf8');
const dom = new JSDOM(html, {
  url: 'https://example.test/Gyne/obg-mastery-path.html',
  runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc,
});
const { window: w } = dom;
const click = (selector) => {
  const el = w.document.querySelector(selector);
  assert.ok(el, `Missing interactive element ${selector}`);
  el.click();
};
const state = expr => w.eval(expr);
assert.match(w.document.body.textContent, /44 of 49 chapters built/);
click('[data-a="toggleUnlock"]');
click('[data-a="goBrowse"]');
for (let ch = 1; ch <= 44; ch++) {
  assert.ok(w.document.querySelector(`[data-a="openChapter"][data-id="ch${String(ch).padStart(2,'0')}"]`));
}
assert.equal(w.document.querySelectorAll('[data-a="openChapter"]').length, 44);
// A prior chapter's progress must not be overwritten by new chapter progress.
w.eval("S.stats['ch01-u1-q1'] = {box:2,nextReview:'2027-01-01',timesWrong:1,timesCorrect:3}; persist();");
let count = 0;
for (let ch = 41; ch <= 44; ch++) {
  click(`[data-a="openChapter"][data-id="ch${ch}"]`);
  const ids = Array.from(w.document.querySelectorAll('[data-a="startUnit"]'), e => e.dataset.id);
  assert.ok(ids.length);
  for (const id of ids) {
    click(`[data-a="startUnit"][data-id="${id}"]`);
    const expectedIds = JSON.parse(state('JSON.stringify(S.queue.map(q => q.id))'));
    assert.equal(expectedIds[0], `${id}-q1`);
    let index = 0;
    while (state('S.view') === 'quiz') {
      assert.equal(state('S.queue[S.qIndex].id'), expectedIds[index++]);
      assert.equal(w.document.querySelectorAll('[data-a="select"]').length, 4);
      const correct = state('S.queue[S.qIndex].correct');
      const answer = count === 0 ? (correct + 1) % 4 : correct;
      click(`[data-a="select"][data-i="${answer}"]`);
      assert.ok(state('S.revealed'));
      assert.ok(w.document.body.textContent.includes(state('S.queue[S.qIndex].why')));
      assert.equal(w.document.querySelectorAll('[data-a="select"]').length, 0);
      click('[data-a="next"]');
      count++;
    }
    assert.equal(index, expectedIds.length);
    assert.match(w.document.body.textContent, /Session complete/);
    click('[data-a="leaveQuiz"]');
    assert.ok(state(`isUnitDone(ALL_UNITS.find(u => u.id === '${id}'))`));
  }
  click('[data-a="goBrowse"]');
  console.log(`ch${ch}: all ${ids.length} units playable, in source order, explanations and completion work`);
}
assert.equal(count, 517);
const saved = JSON.parse(w.localStorage.getItem(state('STORE_KEY')));
assert.equal(saved.stats['ch01-u1-q1'].timesCorrect, 3);
assert.equal(Object.keys(saved.stats).filter(id => /^ch(41|42|43|44)-/.test(id)).length, 517);
assert.equal(saved.stats['ch41-u1-q1'].timesWrong, 1);
w.eval("go('home')");
click('[data-a="reviewMistakes"]');
assert.ok(state("S.queue.some(q => q.id === 'ch41-u1-q1')"));
assert.equal(errors.length, 0, errors.map(String).join('\n'));
const reload = new JSDOM(html, {
  url: 'https://example.test/Gyne/obg-mastery-path.html', runScripts: 'dangerously',
  pretendToBeVisual: true, virtualConsole: vc,
  beforeParse(win) { win.localStorage.setItem(state('STORE_KEY'), JSON.stringify(saved)); },
});
assert.equal(reload.window.eval("S.stats['ch44-u13-q18'].timesCorrect"), 1);
assert.equal(reload.window.eval("S.stats['ch01-u1-q1'].timesCorrect"), 3);
assert.equal(errors.length, 0);
reload.window.close();
w.close();
console.log('PASS: 517 new questions; saved progress survives reload; legacy progress retained; mistake review works.');
