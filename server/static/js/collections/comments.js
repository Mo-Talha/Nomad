require(['lib/jquery', 'lib/backbone', 'js/models/comment'], function($, Backbone, Comment) {

    var Comments = Backbone.Collection.extend({

        model: Comment,

        url: '/api/comment',

        comparator: function(model) {
            return model.get('date').getTime();
        }

    });

    return Comments;

});
