define(['lib/jquery', 'lib/underscore', 'lib/backbone',
    'hbs!js/views/comments/comment'
], function ($, _, Backbone, CommentTemplate) {
	'use strict';

	var CommentView = Backbone.View.extend({

		tagName: 'div',

		className: 'job-comment-container',

		template: CommentTemplate,

		initialize: function () {
			this.listenTo(this.model, 'change', this.render);
			this.listenTo(this.model, 'destroy', this.remove);
		},

		render: function () {
			this.$el.html(this.template(_.extend(this.model.toJSON(), this._addRatings(this.model.get('rating')))));
			return this;
		},

		clear: function () {
			this.model.destroy();
		},

        _addRatings: function(rating){
		    var i;
            var star_classes = [];

            for (i = 1; i <= rating; i++){
                star_classes.push('fa-star');
            }

            if (rating % 1 != 0){
                star_classes.push('fa-star-half-o');
            }

            while (i <= 5 && star_classes.length < 5) {
                star_classes.push('fa-star-o');
                i++;
            }

            return {
                ratings: star_classes
            };
        }
	});

	return CommentView;
});