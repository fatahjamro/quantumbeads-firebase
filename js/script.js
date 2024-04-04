window.onload = function() {
  document.querySelectorAll('.subfield').forEach(item => {
    item.addEventListener('click', event => {
      document.querySelectorAll('.subfield-content').forEach(content => {
        content.style.display = 'none';
      });
      document.getElementById(item.dataset.target).style.display = 'block';
    });
  });
};