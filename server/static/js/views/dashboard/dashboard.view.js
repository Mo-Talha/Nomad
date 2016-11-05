define(['lib/backbone', 'lib/underscore', 'lib/jquery',
        'js/views/chart/programsvsjobs.view',
        'js/views/chart/jobsvslevels'],
    function(Backbone, _, $, ProgramsVsJobsView, JobsVsLevelsView){

    var DashboardView = Backbone.View.extend({

        tagName: 'div',

        className: 'dashboard',

        template: false,

        initialize: function(options) {
            this.options = options || {};
            this.programsVsJobsChart = new ProgramsVsJobsView(options);
            this.jobsVsLevelsChart = new JobsVsLevelsView(options);
        },

        events: {

        },

        render: function() {
            this.$el.append(this.programsVsJobsChart.render().el);
            this.$el.append(this.jobsVsLevelsChart.render().el);
            return this;
        }
    });

    return DashboardView;
});