define(['lib/jquery', 'lib/underscore', 'lib/backbone',
	'hbs!js/views/comments/commentrating'
], function ($, _, Backbone, CommentRatingTemplate) {
	'use strict';

	var CommentRatingView = Backbone.View.extend({

	    tagName: 'div',

        className: 'add-comment-rating-container',

        events: {
	      'click .add-comment-rating': 'onClick'
        },

		template: CommentRatingTemplate,

        initialize: function () {
	        this.rating = 0;
	        this.enable = true;
		},

		render: function () {
	        this.$el.html(this.template(this.model.toJSON()));
    		return this;
		},

        onClick: function(e){
            var $this = this.$('.add-comment-rating');

            var currentMousePosition = e.pageX - $this.offset().left;
            var width = $this.width();
            var rounded = Math.round((currentMousePosition/width)*10);

            this.rating = rounded / 2;

            this.model.set('ratings', this._addRatings(this.rating));
            this.model.set('rating', this.rating);
            this.render();
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

            return star_classes;
        }
	});

	return CommentRatingView;
});