(function () {
  function get(k) { try { return localStorage.getItem('wws-' + k); } catch (e) { return null; } }
  function set(k, v) { try { if (v === null) localStorage.removeItem('wws-' + k); else localStorage.setItem('wws-' + k, v); } catch (e) {} }
  document.querySelectorAll('.choice').forEach(function (b) {
    b.addEventListener('click', function () {
      var fb = document.getElementById(b.getAttribute('aria-controls'));
      var open = b.getAttribute('aria-expanded') === 'true';
      b.setAttribute('aria-expanded', open ? 'false' : 'true');
      fb.hidden = open;
    });
  });
  document.querySelectorAll('textarea[data-key]').forEach(function (t) {
    var k = t.getAttribute('data-key');
    t.value = get(k) || '';
    t.addEventListener('input', function () { set(k, t.value || null); });
  });
  document.querySelectorAll('input[data-done]').forEach(function (c) {
    var k = 'done-' + c.getAttribute('data-done');
    c.checked = get(k) === '1';
    c.addEventListener('change', function () { set(k, c.checked ? '1' : null); });
  });
  document.querySelectorAll('[data-status]').forEach(function (s) {
    if (get('done-' + s.getAttribute('data-status')) === '1') { s.classList.add('is-done'); s.setAttribute('aria-label', 'Finished'); }
  });
})();
