define(['lib/jquery', 'lib/underscore', 'lib/backbone',
	'js/models/rating.model',
    'js/views/comments/comment.view',
    'js/views/comments/commentrating.view',
    'js/models/comment.model',
    'js/util',
	'hbs!js/views/comments/comments'
], function ($, _, Backbone, RatingModel, CommentView, CommentRatingView,
             CommentModel, Util, CommentsTemplate) {
	'use strict';

	var CommentsView = Backbone.View.extend({

	    className: 'job-comments',

		template: CommentsTemplate,

		events: {
			'keypress .job-add-comment': 'addComment'
		},

        initialize: function () {
	        this.listenTo(this.collection, 'add', this.render);
		},

		render: function () {
            this.$el.html(this.template());

            this.commentRatingView = new CommentRatingView({model: new RatingModel()});
            this.$('.job-add-comment-rating').append(this.commentRatingView.render().el);

            if (this.collection.length > 0){
                this.collection.each(function(comment) {
                    var commentView = new CommentView({ model: comment });
                    this.$('.job-comments-container').append(commentView.render().el);
                }, this);
            }

    		return this;
		},

		addComment: function (e) {
	        var self = this;
			var $comment = this.$('.job-add-comment');
			var $salary = this.$('.job-add-comment-salary');

			if (e.which !== 13 || !$comment.val().trim() || ($salary.val().trim() == '')) {
				return;
			}

			this.collection.create({
			    id: window.job_id,
                text: $comment.val().trim(),
                date: new Date(),
                date_formatted: Util._convertToFormattedDate(new Date()),
                salary: $salary.val().trim(),
                rating: this.commentRatingView.model.get('rating'),
                crawled: false
            }, {
			    at: 0,
                wait : true,
                success : function () {
                    self.render();
                }
            });
		}
	});

	return CommentsView;
});