define(['lib/jquery', 'lib/backbone', 'js/models/comment.model'],
    function($, Backbone, Comment) {

    var Comments = Backbone.Collection.extend({

        model: Comment,

        url: '/api/comment',

        comparator: function(model) {
            return -(new Date(model.get('date')).getTime());
        }

    });

    return Comments;

});
