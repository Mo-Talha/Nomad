define(['lib/jquery'], function($) {

    $(document).ready(function(){
        $('.navbar-searchbar').on('keyup keypress', function(e) {
          var keyCode = e.keyCode || e.which;
          if (keyCode === 13 && !$(this).val()) {
            e.preventDefault();
            return false;
          }
        });
    });

});