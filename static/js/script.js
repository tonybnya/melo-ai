// current date in header and footer components
(function () {
  const d = new Date();
  document.getElementById('footer-year').textContent = d.getFullYear();
  document.getElementById('current-date').textContent = d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
})();

// tag labels per question index
const Q_TAGS = ['Technical & Functional', 'Situational Judgment', 'Culture & Behaviour'];
// DOM references
const inputEl = document.getElementById('job-title-input');
const submitBtn = document.getElementById('submit-btn');
const loader = document.getElementById('loader');
const errorBox = document.getElementById('error-box');
const resultsSection = document.getElementById('results-section');
const roleLabel = document.getElementById('results-role-label');
const container = document.getElementById('questions-container');

// event listeners
submitBtn.addEventListener('click', handleSubmit);
inputEl.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') handleSubmit();
});
