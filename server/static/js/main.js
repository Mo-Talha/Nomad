require.config({
    shim: {
        'lib/backbone': {
            deps: ['lib/jquery', 'lib/underscore'],
            exports: 'Backbone'
        },
        'lib/underscore': {
            exports: '_'
        },
        'lib/jquery': {
            exports: '$'
        },
        'lib/chartjs': {
            exports: 'Chart'
        },
        'lib/hbs': {
            exports: 'Handlebars'
        }
    },
    baseUrl: '/static/',
    paths: {
        'lib/backbone': 'lib/backbone/backbone',
        'lib/underscore': 'lib/underscore/underscore',
        'lib/jquery': 'lib/jquery/dist/jquery',
        'lib/bootstrap': 'lib/bootstrap/dist/js/bootstrap',
        'lib/chartjs': 'lib/chart.js/dist/Chart',
        'lib/hbs': 'lib/require-handlebars-plugin/hbs',
         hbs: 'lib/require-handlebars-plugin/hbs',
         async: 'lib/requirejs-plugins/src/async',
        'index': 'js/index',
        'job': 'js/job',
        'search': 'js/search',
        'cs': 'js/cs'
    },
    hbs: {
        helpers: true,
        templateExtension: 'hbs',
        partialsUrl: ''
    }
});

if (window.script) {
    require([window.script]);
}