// Edabit Python challenges scraper
// Usage: paste into browser console while logged in on Edabit.
// It will create one JSON download per difficulty (very easy, easy, medium, hard, very hard, expert).
// Targets: 300 challenges per difficulty (or as many as available).
// Notes: Site structure may change; adjust selectors if needed.

(async () => {
  const LIST_URL = location.href;
  const DIFFICULTIES = [
    { label: 'very_easy', ui: 'Very Easy' },
    { label: 'easy', ui: 'Easy' },
    { label: 'medium', ui: 'Medium' },
    { label: 'hard', ui: 'Hard' },
    { label: 'very_hard', ui: 'Very Hard' },
    { label: 'expert', ui: 'Expert' },
  ];

  const TARGET_PER_DIFF = 300;
  const LANGUAGE_UI = 'Python';

  function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

  function downloadJSON(filename, data) {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }

  function uniq(arr) {
    return Array.from(new Set(arr));
  }

  function getChallengeLinks() {
    // Try common patterns: anchor tags that link to /challenge/... or /challenge/slug
    const anchors = Array.from(document.querySelectorAll('a[href]'));
    const links = anchors
      .map(a => a.getAttribute('href'))
      .filter(h => h && (h.includes('/challenge/') || h.includes('/challenge/')))
      .map(h => h.startsWith('http') ? h : location.origin + h);
    return uniq(links);
  }

  function findButtonByText(text) {
    const buttons = Array.from(document.querySelectorAll('button, a'));
    return buttons.find(b => b.textContent && b.textContent.trim().toLowerCase().includes(text.toLowerCase()));
  }

  function isInteractive(node) {
    if (!node) return false;
    const role = node.getAttribute && node.getAttribute('role');
    const tabindex = node.getAttribute && node.getAttribute('tabindex');
    if (role === 'button' || role === 'listbox' || role === 'menu') return true;
    if (tabindex && tabindex !== '-1') return true;
    if (node.tagName === 'BUTTON' || node.tagName === 'A') return true;
    return false;
  }

  function findClickableByExactText(text) {
    const nodes = Array.from(document.querySelectorAll('button, a, li, div, span'));
    return nodes.find(n => isInteractive(n) && n.textContent && n.textContent.trim() === text && !isChallengeLink(n));
  }

  function isChallengeLink(node) {
    const link = node.closest && node.closest('a[href]');
    if (!link) return false;
    const href = link.getAttribute('href') || '';
    return href.includes('/challenge/');
  }

  function findOptionInOpenMenu(text) {
    // Prefer ARIA listbox/option pattern used by Edabit
    const ariaOptions = Array.from(document.querySelectorAll('[role="option"]'))
      .filter(n => n.textContent && n.textContent.trim() === text);
    const visibleAria = ariaOptions.find(n => n.offsetParent !== null);
    if (visibleAria) return visibleAria;

    const menus = Array.from(document.querySelectorAll('[role="listbox"], [role="menu"], ul, ol, .dropdown, .menu'));
    const visibleMenus = menus.filter(m => m.offsetParent !== null);
    for (const menu of visibleMenus) {
      const option = Array.from(menu.querySelectorAll('button, a, li, div, span'))
        .find(n => n.textContent && n.textContent.trim() === text && !isChallengeLink(n));
      if (option) return option;
    }
    return null;
  }

  async function openDropdownByLabel(labelText) {
    const btn = findButtonByText(labelText);
    if (!btn) return false;
    btn.click();
    await sleep(500);
    return true;
  }

  async function openDropdownByCurrentValue(currentValueText) {
    const el = findClickableByExactText(currentValueText);
    if (el) {
      el.click();
      await sleep(500);
      return true;
    }
    // If the current value is inside a non-interactive text span, click its parent
    const span = Array.from(document.querySelectorAll('span'))
      .find(n => n.textContent && n.textContent.trim() === currentValueText);
    if (span && span.parentElement) {
      span.parentElement.click();
      await sleep(500);
      return true;
    }
    return false;
  }

  async function selectDropdownOption(optionText) {
    const option = findOptionInOpenMenu(optionText) || findClickableByExactText(optionText);
    if (!option) return false;
    option.click();
    await sleep(800);
    return true;
  }

  async function setLanguageToPython() {
    // Heuristic: open language filter and pick Python.
    // Adjust selectors as needed.
    // Common patterns: buttons or dropdowns with text.
    const opened =
      await openDropdownByLabel('Language') ||
      await openDropdownByLabel('Languages') ||
      await openDropdownByCurrentValue('JavaScript') ||
      await openDropdownByCurrentValue('Python');
    if (!opened) return false;
    const selected = await selectDropdownOption(LANGUAGE_UI);
    if (selected) {
      console.log('Selected language: Python');
      return true;
    }
    // Fallback: try clicking any visible Python option again
    const pyOption = findClickableByExactText(LANGUAGE_UI);
    if (pyOption) {
      pyOption.click();
      await sleep(800);
      console.log('Selected language: Python (fallback)');
      return true;
    }
    console.warn('Could not select Python language option');
    return false;
  }

  async function setDifficulty(diff) {
    // Heuristic: open difficulty filter and click.
    const opened =
      await openDropdownByLabel('Difficulty') ||
      await openDropdownByLabel('Difficulties') ||
      await openDropdownByCurrentValue('Very Easy') ||
      await openDropdownByCurrentValue('Easy') ||
      await openDropdownByCurrentValue('Medium') ||
      await openDropdownByCurrentValue('Hard') ||
      await openDropdownByCurrentValue('Very Hard') ||
      await openDropdownByCurrentValue('Expert');
    if (!opened) return false;
    return await selectDropdownOption(diff.ui);
  }

  async function loadEnoughChallenges(target) {
    let lastCount = 0;
    for (let i = 0; i < 50; i++) {
      window.scrollTo(0, document.body.scrollHeight);
      await sleep(1200);
      // Try a "Load More" button if present
      const loadBtn = findButtonByText('load');
      if (loadBtn) {
        loadBtn.click();
        await sleep(1200);
      }
      const count = getChallengeLinks().length;
      if (count >= target) break;
      if (count === lastCount) {
        // No new items loading; break
        break;
      }
      lastCount = count;
    }
  }

  async function fetchChallengeDetail(url) {
    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        const res = await fetch(url, { credentials: 'include' });
        const html = await res.text();
        if (/too many requests/i.test(html) || res.status === 429) {
          console.warn('Too many requests; backing off 60s');
          await sleep(60000);
          continue;
        }

        const doc = new DOMParser().parseFromString(html, 'text/html');

        const title = (doc.querySelector('h1') || doc.querySelector('h2') || {}).textContent?.trim() || '';
        const difficulty = diffLabelFromDoc(doc);
        const description = extractDescription(doc);
        const tests = extractTests(doc);

        return { url, title, difficulty, description, tests };
      } catch (e) {
        if (attempt === 2) {
          return { url, title: '', difficulty: '', description: '', tests: [], error: String(e) };
        }
        await sleep(5000);
      }
    }
  }

  function diffLabelFromDoc(doc) {
    // Try to find difficulty label in page text
    const text = doc.body ? doc.body.innerText : '';
    const match = text.match(/Very Easy|Easy|Medium|Hard|Very Hard|Expert/);
    return match ? match[0] : '';
  }

  function extractDescription(doc) {
    // Common patterns: challenge description block
    const candidates = Array.from(doc.querySelectorAll('article, section, .challenge, .description, .content'));
    for (const el of candidates) {
      const text = el.innerText ? el.innerText.trim() : '';
      if (text && text.length > 40) return text;
    }
    const p = doc.querySelector('p');
    return p ? p.innerText.trim() : '';
  }

  function extractTests(doc) {
    // Heuristic: look for "Examples" or code/pre blocks.
    const blocks = Array.from(doc.querySelectorAll('pre, code'))
      .map(el => el.innerText.trim())
      .filter(t => t && t.length > 0);
    return blocks;
  }

  async function runForDifficulty(diff) {
    console.log(`Starting difficulty: ${diff.ui}`);
    // Navigate to Edabit challenge browse page if not already there
    // This assumes you are already on the challenge list page.
    if (location.href !== LIST_URL) {
      location.href = LIST_URL;
      await sleep(1500);
    }

    await setLanguageToPython();
    await setDifficulty(diff);

    await loadEnoughChallenges(TARGET_PER_DIFF);

    const links = getChallengeLinks().slice(0, TARGET_PER_DIFF);
    console.log(`Collected ${links.length} links for ${diff.ui}`);

    const results = [];
    for (let i = 0; i < links.length; i++) {
      const url = links[i];
      const detail = await fetchChallengeDetail(url);
      results.push(detail);
      if (i % 10 === 0) console.log(`${diff.ui}: ${i}/${links.length}`);
      await sleep(1500);
      if (i > 0 && i % 20 === 0) await sleep(10000);
    }

    downloadJSON(`edabit_${diff.label}.json`, results);
    console.log(`Done ${diff.ui}`);
  }

  for (const diff of DIFFICULTIES) {
    await runForDifficulty(diff);
    await sleep(1500);
  }

  console.log('All difficulties done');
})();
