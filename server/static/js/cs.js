require(['lib/jquery', 'js/views/dashboard/csdashboard.view'],
    function($, CSDashboardView) {

    $('.navbar-menu').click(function(){
        $('.navbar-items').animate({height: 'toggle'}, 200);
    });

    var dashboard = new CSDashboardView();

    $('.dashboard-container').html(dashboard.render().el);

});