// Initialize Bootstrap toasts after DOM is ready
// Requires jQuery and Bootstrap JS to be loaded first
(function($) {
  $(function() {
    $('.toast').toast('show');
  });
})(jQuery);

