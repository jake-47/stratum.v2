// Table of Contents highlighting on scroll
document.addEventListener('DOMContentLoaded', function() {
  const tocLinks = document.querySelectorAll('.md-sidebar--secondary .md-nav__link');
  const headings = document.querySelectorAll('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]');
  
  function updateTOCHighlight() {
    let current = '';
    
    headings.forEach(heading => {
      const rect = heading.getBoundingClientRect();
      if (rect.top <= 100) {
        current = heading.id;
      }
    });
    
    tocLinks.forEach(link => {
      link.classList.remove('md-nav__link--in-view');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('md-nav__link--in-view');
      }
    });
  }
  
  window.addEventListener('scroll', updateTOCHighlight);
  updateTOCHighlight(); // Initial call
});