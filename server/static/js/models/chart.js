define(['lib/backbone', 'lib/underscore'], function (Backbone, _) {

    var Chart = Backbone.Model.extend({
        defaults: {
            title: '',
            completed: false
        }
    });

    return Chart;
});