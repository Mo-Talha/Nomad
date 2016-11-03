define(['lib/backbone', 'lib/underscore', 'lib/jquery',
        'js/views/chart/mostpopularprograms.view'],
    function(Backbone, _, $, MostPopularProgramsChart){

    var DashboardView = Backbone.View.extend({

        tagName: 'div',

        className: 'dashboard',

        template: false,

        initialize: function(options) {
            this.options = options || {};
            this.mostPopularProgramsChart = new MostPopularProgramsChart(options);
        },

        events: {

        },

        render: function() {
            this.$el.html(this.mostPopularProgramsChart.render().el);
            return this;
        }
    });

    return DashboardView;
});