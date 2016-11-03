var paths = {
    'lib/backbone': 'lib/backbone/backbone',
    'lib/underscore': 'lib/underscore/underscore',
    'lib/jquery': 'lib/jquery/dist/jquery',
    'lib/bootstrap': 'lib/bootstrap/dist/js/bootstrap',
    'lib/chartjs': 'lib/chart.js/dist/Chart',
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
    paths: paths,
    hbs: {
        helpers: true,
        templateExtension: 'hbs',
        partialsUrl: ''
    }
});

if (window.script) {
    require([window.script]);
}