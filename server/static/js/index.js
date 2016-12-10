define(['lib/jquery', 'js/views/dashboard/dashboard.view', 'js/search'],
    function($, DashboardView) {

    $('.navbar-menu').click(function(){
        $('.navbar-items').animate({height: 'toggle'}, 200);
    });

    $(document).ready(function(){
        var generalDashboard = new DashboardView();

        $('.dashboard-container').html(generalDashboard.render().el);
    });

});