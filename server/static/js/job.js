require(['lib/jquery', 'js/search'],
    function($) {

    $('.navbar-menu').click(function(){
        $('.navbar-items').animate({height: 'toggle'}, 200);
    });

});