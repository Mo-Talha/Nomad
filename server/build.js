({
   baseUrl: 'static/',
   mainConfigFile: 'static/js/main.js',
   out: 'static/dist/bundle.js',
   preserveLicenseComments: false,
   removeCombined: true,
   findNestedDependencies: true,
   optimize: 'none',
   optimizeCss: "standard",
   paths: {
       'lib/backbone': 'lib/backbone/backbone',
       'lib/underscore': 'lib/underscore/underscore',
       'lib/jquery': 'lib/jquery/dist/jquery',
       'lib/chartjs': 'lib/chart.js/dist/Chart',
       'lib/hbs': 'lib/require-handlebars-plugin/hbs',
       'async': 'lib/requirejs-plugins/src/async'
   },
   include: ['lib/jquery', 'lib/backbone', 'lib/underscore', 'lib/chartjs',
             'lib/hbs', 'async', 'js/index', 'js/cs', 'js/job'],
   stubModules: ['lib/hbs/json2', 'lib/hbs/handlebars']
})