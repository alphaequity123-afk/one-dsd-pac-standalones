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
  document.querySelectorAll('.done-btn').forEach(function (b) {
    var k = 'done-' + b.getAttribute('data-done');
    function show(on) { b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.textContent = on ? 'Finished. Select again to undo.' : 'Mark this module finished'; }
    show(get(k) === '1');
    b.addEventListener('click', function () { var on = b.getAttribute('aria-pressed') !== 'true'; set(k, on ? '1' : null); show(on); });
  });
  document.querySelectorAll('[data-status]').forEach(function (s) {
    if (get('done-' + s.getAttribute('data-status')) === '1') { s.classList.add('is-done'); s.textContent = 'Finished'; }
  });
})();
