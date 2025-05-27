// Simple, direct approach - no MutationObserver
function updateTitles() {
  const left = document.querySelector('.md-sidebar--primary .md-nav__title');
  const right = document.querySelector('.md-sidebar--secondary .md-nav__title');
  
  if (left) left.textContent = 'Contents';
  if (right) right.textContent = 'On this page';
}

// Run on load and on every page change
document.addEventListener('DOMContentLoaded', updateTitles);
setInterval(updateTitles, 500); // Check every 500ms