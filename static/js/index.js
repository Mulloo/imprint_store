document.addEventListener('DOMContentLoaded', function() {
    const scrollIndicator = document.querySelector('.scroll-indicator');
    const newsletterSection = document.querySelector('.newsletter-peek');
    
    if (scrollIndicator && newsletterSection) {
        scrollIndicator.addEventListener('click', function(e) {
            e.preventDefault();
            setTimeout(function() {
                newsletterSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 100);
        });
    }
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    const animateElements = document.querySelectorAll('.hero-content, .newsletter-peek');
    animateElements.forEach(element => {
        observer.observe(element);
    });
});
