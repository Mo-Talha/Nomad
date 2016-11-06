define(['lib/backbone', 'lib/underscore', 'lib/jquery',
        'js/views/chart/programsvsjobs.view',
        'js/views/chart/jobsvslevels.view',
        'js/views/chart/jobsvsterms.view'],
    function(Backbone, _, $, ProgramsVsJobsView, JobsVsLevelsView, JobsVsTermsView){

    var DashboardView = Backbone.View.extend({

        tagName: 'div',

        className: 'dashboard',

        template: false,

        initialize: function(options) {
            this.options = options || {};
            this.programsVsJobsChart = new ProgramsVsJobsView(options);
            this.jobsVsLevelsChart = new JobsVsLevelsView(options);
            this.jobsVsTermsChart = new JobsVsTermsView(options);
        },

        events: {

        },

        render: function() {
            this.$el.append(this.programsVsJobsChart.render().el);
            this.$el.append(this.jobsVsLevelsChart.render().el);
            this.$el.append(this.jobsVsTermsChart.render().el);
            return this;
        }
    });

    return DashboardView;
});