// current date in header
(function () {
  const d = new Date();
  document.getElementById('current-date').textContent = d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
})();
