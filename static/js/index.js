document.addEventListener('DOMContentLoaded', function() {
    console.log('Index.js loaded');
    
    // Smooth scroll for the scroll indicator
    const scrollIndicator = document.querySelector('.scroll-indicator');
    const newsletterSection = document.querySelector('.newsletter-peek');
    
    console.log('Scroll indicator found:', scrollIndicator);
    console.log('Newsletter section found:', newsletterSection);
    
    if (scrollIndicator && newsletterSection) {
        console.log('Setting up scroll indicator click handler');
        scrollIndicator.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Scroll indicator clicked');
            
            // Add a slight delay for better UX
            setTimeout(function() {
                newsletterSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 100);
        });
    } else {
        console.log('Missing elements:', {
            scrollIndicator: !!scrollIndicator,
            newsletterSection: !!newsletterSection
        });
    }
    
    // Add scroll-based animations
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
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.hero-content, .newsletter-peek');
    animateElements.forEach(element => {
        observer.observe(element);
    });
});