define(['lib/backbone', 'lib/underscore', 'lib/jquery',
        'js/views/chart/jobsvsprogramminglanguages.view',
        'js/views/chart/jobsvsdatabases.view',
        'js/views/chart/jobsvsoperatingsystems.view',
        'js/views/chart/jobsvswebframeworks.view',
        'js/views/chart/jobsvsapacheframeworks.view',
        'js/views/chart/jobsvsjavascriptlibraries.view',
        'js/views/chart/jobsvscssframeworks.view'],
    function(Backbone, _, $, JobsVsProgrammingLanguages, JobsVsDatabases, JobsVsOS, JobsVsWebFrameworks,
            JobsVsApacheFrameworks, JobsVsJavaScriptLibraries, JobsVsCssFrameworks){

    var CSDashboardView = Backbone.View.extend({

        tagName: 'div',

        className: 'dashboard',

        template: false,

        initialize: function(options) {
            this.options = options || {};
            this.jobsVsProgrammingLanguages = new JobsVsProgrammingLanguages(options);
            this.jobsVsDatabases = new JobsVsDatabases(options);
            this.jobsVsOS = new JobsVsOS(options);
            this.jobsVsWebFrameworks = new JobsVsWebFrameworks(options);
            this.jobsVsApacheFrameworks = new JobsVsApacheFrameworks(options);
            this.jobsVsJavaScriptLibraries = new JobsVsJavaScriptLibraries(options);
            this.jobsVsCssFrameworks = new JobsVsCssFrameworks(options);
        },

        render: function() {
            this.$el.append(this.jobsVsProgrammingLanguages.render().el);
            this.$el.append(this.jobsVsDatabases.render().el);
            this.$el.append(this.jobsVsOS.render().el);
            this.$el.append(this.jobsVsWebFrameworks.render().el);
            this.$el.append(this.jobsVsApacheFrameworks.render().el);
            this.$el.append(this.jobsVsJavaScriptLibraries.render().el);
            this.$el.append(this.jobsVsCssFrameworks.render().el);
            return this;
        }
    });

    return CSDashboardView ;
});