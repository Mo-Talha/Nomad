define(['lib/jquery', 'js/views/dashboard/csdashboard.view', 'js/search'],
    function($, CSDashboardView) {

    $('.navbar-menu').click(function(){
        $('.navbar-items').animate({height: 'toggle'}, 200);
    });

    $(document).ready(function(){
        var dashboard = new CSDashboardView();

        $('.dashboard-container').html(dashboard.render().el);
    });

});