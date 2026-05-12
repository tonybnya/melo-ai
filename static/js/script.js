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

// state helpers
function setLoading(on) {
  submitBtn.disabled = on;
  loader.classList.toggle('visible', on);
}

function showError(msg) {
  errorBox.textContent = '⚠ ' + msg;
  errorBox.classList.add('visible');
}

function clearError() {
  errorBox.textContent = '';
  errorBox.classList.add('visible');
}

function renderQuestions(jobTitle, questions) {
  roleLabel.textContent = jobTitle;
  container.innerHTML = '';

  questions.forEach(function (q, i) {
    const card = document.createElement('div');
    card.className = 'question-card';
    card.style.animationDelay = (i * 0.12) + 's';

    card.innerHTML = `
      <div class="q-number">0${i + 1}</div>
      <div>
        <div class="q-tag">${Q_TAGS[i] || 'Question'}</div>
        <p class="q-text">${escapeHtml(q)}</p>
      </div>`;

    container.appendChild(card);
  });

  resultsSection.classList.add('visible');
  resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// submit handler
async function handleSubmit() {
  cons jobTitle = inputEl.value.trim();

  clearError();
  resultsSection.classList.remove('visible');

  if(!jobTitle) {
    showError('Please enter a job title before submitting.');
    inputEl.focus();
    return;
  }

  setLoading(true);

  try {
    const response = await fetch('/api/questions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ job_title: jobTitle }),
    });

    const data = await response.json();

    if (!response.ok) {
      showError(data.error || 'Something went wrong. Please try again.');
      return;
    }

    renderQuestions(jobTitle, data.questions);

  } catch (err) {
    showError('Network error - please check your connection and try again.');
  } finally {
    setLoading(false);
  }
}

// event listeners
submitBtn.addEventListener('click', handleSubmit);
inputEl.addEventListener('keydown', function (e) {
  if (e.key === 'Enter') handleSubmit();
});
