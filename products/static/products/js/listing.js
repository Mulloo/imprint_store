// Product listing page behaviors (sorting and back-to-top)
(function($) {
  $(function() {
    // Back-to-top smooth scroll
    $('.btt-link').on('click', function(e) {
      e.preventDefault();
      window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
    });

    // Sort handler
    $('#sort-selector').on('change', function () {
      var selectedVal = $(this).val();
      var currentUrl = new URL(window.location);

      if (selectedVal !== 'reset') {
        var parts = selectedVal.split('_');
        var sort = parts[0];
        var direction = parts[1];
        currentUrl.searchParams.set('sort', sort);
        currentUrl.searchParams.set('direction', direction);
      } else {
        currentUrl.searchParams.delete('sort');
        currentUrl.searchParams.delete('direction');
      }
      window.location.replace(currentUrl.toString());
    });
  });
})(jQuery);

