({
   baseUrl: 'static/',
   mainConfigFile: 'static/js/main.js',
   out: 'static/dist/bundle.js',
   preserveLicenseComments: false,
   removeCombined: false,
   findNestedDependencies: true,
   optimize: 'uglify2',
   optimizeCss: 'standard',
   paths: {
       'lib/backbone': 'lib/backbone/backbone',
       'lib/underscore': 'lib/underscore/underscore',
       'lib/jquery': 'lib/jquery/dist/jquery',
       'lib/chartjs': 'lib/chart.js/dist/Chart',
       'lib/hbs': 'lib/require-handlebars-plugin/hbs',
       'async': 'lib/requirejs-plugins/src/async',
       'index': 'js/index',
       'job': 'js/job',
       'cs': 'js/cs'
   },
   name: "js/main",
   include: ['lib/jquery', 'lib/underscore', 'lib/backbone', 'lib/chartjs',
             'lib/hbs', 'async', 'index', 'cs', 'job'],
   stubModules: ['lib/hbs/json2', 'lib/hbs/handlebars']
})