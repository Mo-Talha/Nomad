var paths = {
    'lib/backbone': 'lib/backbone/backbone.js',
    'lib/underscore': 'lib/underscore/underscore.js',
    'lib/jquery': 'lib/jquery/dist/jquery.js',
    'lib/bootstrap': 'lib/bootstrap/dist/js/bootstrap.js',
    'lib/chartjs': 'lib/chart.js/dist/Chart.js',
     hbs: 'lib/require-handlebars-plugin/hbs'
};

var shim = {
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
    }
};

require.config({
    shim: shim,
    baseUrl: '/static/',
    paths: paths
});

if (window.script) {
    require([window.script]);
}