// DOM integration test: real event delegation, rendered options, feedback,
// navigation, completion, mistake review and localStorage round-trip across ch36-49.
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
assert.match(w.document.body.textContent, /49 of 49 chapters built/);
click('[data-a="toggleUnlock"]');
click('[data-a="goBrowse"]');
for (let ch = 1; ch <= 49; ch++) {
  assert.ok(w.document.querySelector(`[data-a="openChapter"][data-id="ch${String(ch).padStart(2,'0')}"]`));
}
assert.equal(w.document.querySelectorAll('[data-a="openChapter"]').length, 49);

// Pre-existing progress (both untouched ch01 and baseline ch36-40 IDs) must be preserved
// before and after playing units, including units that open with q0a sub-IDs.
w.eval(`
  S.stats['ch01-u1-q1'] = {box:2,nextReview:'2027-01-01',timesWrong:1,timesCorrect:3};
  S.stats['ch36-u2-q1'] = {box:3,nextReview:'2027-01-02',timesWrong:0,timesCorrect:2};
  S.stats['ch40-u6-q18'] = {box:2,nextReview:'2027-01-03',timesWrong:0,timesCorrect:1};
  persist();
`);
assert.ok(state("ALL_UNITS.some(u => u.id === 'ch36-u2' && u.questions[0].id === 'ch36-u2-q0a')"));

let expectedTotal = 0;
const jsonByUnit = new Map();
for (let ch = 36; ch <= 49; ch++) {
  const meta = JSON.parse(readFileSync(`data/ch${ch}.json`, 'utf8'));
  expectedTotal += meta.questions.length;
  for (const q of meta.questions) {
    const uid = q.id.replace(/-q[0-9a-z]+$/, '');
    if (!jsonByUnit.has(uid)) jsonByUnit.set(uid, []);
    jsonByUnit.get(uid).push(q.id);
  }
}

const preSeededIn36To49 = new Set(['ch36-u2-q1', 'ch40-u6-q18']);
let count = 0;
for (let ch = 36; ch <= 49; ch++) {
  click(`[data-a="openChapter"][data-id="ch${ch}"]`);
  const ids = Array.from(w.document.querySelectorAll('[data-a="startUnit"]'), e => e.dataset.id);
  assert.ok(ids.length);
  for (const id of ids) {
    assert.deepEqual(
      JSON.parse(state(`JSON.stringify(ALL_UNITS.find(u => u.id === '${id}').questions.map(q => q.id))`)),
      jsonByUnit.get(id),
      `Unit definition mismatch for ${id}`,
    );
    click(`[data-a="startUnit"][data-id="${id}"]`);
    const expectedIds = JSON.parse(state('JSON.stringify(S.queue.map(q => q.id))'));
    const expectedUnanswered = jsonByUnit.get(id).filter(qid => !preSeededIn36To49.has(qid));
    assert.deepEqual(expectedIds, expectedUnanswered, `Queue mismatch for ${id}`);
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
assert.equal(count, expectedTotal - preSeededIn36To49.size);
const saved = JSON.parse(w.localStorage.getItem(state('STORE_KEY')));
assert.equal(saved.stats['ch01-u1-q1'].timesCorrect, 3);
assert.equal(saved.stats['ch36-u2-q1'].timesCorrect, 2);
assert.equal(saved.stats['ch40-u6-q18'].timesCorrect, 1);
assert.equal(saved.stats['ch36-u2-q0a'].timesCorrect, 1);
assert.equal(Object.keys(saved.stats).filter(id => /^ch(3[6-9]|4[0-9])-/.test(id)).length, expectedTotal);
assert.equal(saved.stats['ch36-u1-q1'].timesWrong, 1);
w.eval("go('home')");
click('[data-a="reviewMistakes"]');
assert.ok(state("S.queue.some(q => q.id === 'ch36-u1-q1')"));
assert.equal(errors.length, 0, errors.map(String).join('\n'));
const reload = new JSDOM(html, {
  url: 'https://example.test/Gyne/obg-mastery-path.html', runScripts: 'dangerously',
  pretendToBeVisual: true, virtualConsole: vc,
  beforeParse(win) { win.localStorage.setItem(state('STORE_KEY'), JSON.stringify(saved)); },
});
assert.equal(reload.window.eval("S.stats['ch40-u6-q18'].timesCorrect"), 1);
assert.equal(reload.window.eval("S.stats['ch36-u2-q1'].timesCorrect"), 2);
assert.equal(reload.window.eval("S.stats['ch36-u2-q0a'].timesCorrect"), 1);
assert.equal(reload.window.eval("S.stats['ch49-u14-q13'].timesCorrect"), 1);
assert.equal(reload.window.eval("S.stats['ch01-u1-q1'].timesCorrect"), 3);
assert.equal(errors.length, 0);
reload.window.close();
w.close();
console.log(`PASS: ${expectedTotal} questions across chapters 36-49; saved progress survives reload; legacy progress retained; mistake review works.`);
