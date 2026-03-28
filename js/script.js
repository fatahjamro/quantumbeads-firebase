// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Toggle abstract functionality
document.addEventListener('DOMContentLoaded', function() {
    // Handle toggle-abstract elements
    document.querySelectorAll('.toggle-abstract').forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const abstractId = this.getAttribute('data-target');
            const abstract = document.getElementById(abstractId);
            if (abstract) {
                abstract.classList.toggle('visible');
                this.textContent = abstract.classList.contains('visible') ? 'Hide abstract' : 'Show abstract';
            }
        });
    });

    // Handle old-style toggle-abstract (with inline hidden content)
    const oldAbstractToggle = document.getElementById('toggle-abstract');
    if (oldAbstractToggle) {
        oldAbstractToggle.addEventListener('click', function() {
            const abstract = document.getElementById('abstract');
            if (abstract) {
                abstract.style.display = abstract.style.display === 'none' || abstract.style.display === '' ? 'block' : 'none';
            }
        });
    }

    // Handle about-me toggle
    const aboutMeToggle = document.getElementById('toggle-about-me');
    if (aboutMeToggle) {
        aboutMeToggle.addEventListener('click', function() {
            const content = document.getElementById('about-me-content');
            if (content) {
                content.style.display = content.style.display === 'none' || content.style.display === '' ? 'block' : 'none';
                this.textContent = content.style.display === 'block' ? 'less...' : 'more...';
            }
        });
    }

    // Handle thumbnail toggle
    const thumbnail = document.getElementById('thumbnail');
    if (thumbnail) {
        thumbnail.addEventListener('click', function() {
            const fullContent = document.getElementById('full-content');
            if (fullContent) {
                fullContent.style.display = fullContent.style.display === 'none' || fullContent.style.display === '' ? 'block' : 'none';
            }
        });
    }

    // Handle subfield clicks
    document.querySelectorAll('.subfield').forEach(item => {
        item.addEventListener('click', event => {
            document.querySelectorAll('.subfield-content').forEach(content => {
                content.style.display = 'none';
            });
            const target = item.dataset.target;
            if (target) {
                const content = document.getElementById(target);
                if (content) {
                    content.style.display = 'block';
                }
            }
        });
    });
});

// Add animation to elements on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.service-card, .about-section, .event-card, .blog-post, .team-member, .publication-item').forEach(el => {
    el.style.opacity = '0';
    observer.observe(el);
});

// Add scroll event listener for navbar background
window.addEventListener('scroll', function() {
    const nav = document.querySelector('nav');
    if (window.scrollY > 0) {
        nav.style.background = 'rgba(10, 10, 26, 0.98)';
    } else {
        nav.style.background = 'rgba(10, 10, 26, 0.95)';
    }
});
