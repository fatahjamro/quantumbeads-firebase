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

// New code for the toggle button
document.getElementById('toggle-abstract').addEventListener('click', function() {
  var abstract = document.getElementById('abstract');
  if (abstract.style.display === 'none' || abstract.style.display === '') {
    abstract.style.display = 'block';
  } else {
    abstract.style.display = 'none';
  }
});

// New code for the About Me toggle button
document.getElementById('toggle-about-me').addEventListener('click', function() {
  var aboutMeContent = document.getElementById('about-me-content');
  if (aboutMeContent.style.display === 'none' || aboutMeContent.style.display === '') {
    aboutMeContent.style.display = 'block';
  } else {
    aboutMeContent.style.display = 'none';
  }
});

document.getElementById('thumbnail').addEventListener('click', function() {
  var fullContent = document.getElementById('full-content');
  if (fullContent.style.display === 'none' || fullContent.style.display === '') {
      fullContent.style.display = 'block';
  } else {
      fullContent.style.display = 'none';
  }
});