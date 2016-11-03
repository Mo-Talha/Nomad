require(['lib/jquery', 'js/views/dashboard/dashboard.view'],
    function($, DashboardView) {

    var generalDashboard = new DashboardView();

    $('.dashboard-container').html(generalDashboard.render().el);

});