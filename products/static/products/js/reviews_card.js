// Reviews functionality for product reviews

// Initialize review functionality when document is ready
$(document).ready(function() {
    initializeReviewFeatures();
});

// Initialize all review-related features
function initializeReviewFeatures() {
    // Add smooth scrolling to reviews section
    if (window.location.hash === '#reviews') {
        scrollToReviews();
    }
    
    // Add confirmation for delete actions
    initializeDeleteConfirmation();
    
    // Add hover effects for review cards
    initializeHoverEffects();
    
    // Add star rating animations
    initializeStarAnimations();
}

// Smooth scroll to reviews section
function scrollToReviews() {
    setTimeout(function() {
        const reviewsSection = document.querySelector('.reviews-section');
        if (reviewsSection) {
            reviewsSection.scrollIntoView({ 
                behavior: 'smooth',
                block: 'start'
            });
        }
    }, 100);
}

// Add confirmation dialog for delete actions
function initializeDeleteConfirmation() {
    $('.btn-outline-danger').click(function(e) {
        e.preventDefault();
        const deleteUrl = $(this).attr('href');
        const reviewTitle = $(this).closest('.card').find('.card-title').text();
        
        if (confirm(`Are you sure you want to delete the review "${reviewTitle}"?\n\nThis action cannot be undone.`)) {
            window.location.href = deleteUrl;
        }
    });
}

// Add subtle hover effects to review cards
function initializeHoverEffects() {
    $('.card').hover(
        function() {
            $(this).addClass('shadow-lg').removeClass('shadow-sm');
        },
        function() {
            $(this).addClass('shadow-sm').removeClass('shadow-lg');
        }
    );
}

// Add animations to star ratings
function initializeStarAnimations() {
    $('.text-warning i').each(function(index) {
        $(this).css('animation-delay', (index * 0.1) + 's');
    });
}

// Utility function to show toast notifications (if you want to add them later)
function showToast(message, type = 'info') {
    // This can be expanded later if you add toast notifications
    console.log(`${type.toUpperCase()}: ${message}`);
}

// Function to handle review voting (if you want to add helpful votes later)
function handleReviewVoting() {
    $('.vote-helpful').click(function(e) {
        e.preventDefault();
        const reviewId = $(this).data('review-id');
        // Add AJAX call to vote endpoint
        showToast('Thank you for your feedback!', 'success');
    });
}