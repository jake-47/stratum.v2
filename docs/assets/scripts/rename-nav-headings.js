document.addEventListener("DOMContentLoaded", function() {
  // Rename left sidebar heading (site title)
  const leftTitle = document.querySelector(".md-sidebar--primary .md-nav__title");
  if (leftTitle) {
    leftTitle.textContent = "Contents";
  }
  
  // Rename right sidebar heading (TOC)
  const rightTitle = document.querySelector(".md-sidebar--secondary .md-nav__title");
  if (rightTitle) {
    rightTitle.textContent = "On this page";
  }
});