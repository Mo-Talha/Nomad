define(['lib/jquery', 'lib/underscore', 'lib/backbone',
    'js/views/comments/comment.view'
], function ($, _, Backbone, CommentView) {
	'use strict';

	var CommentsView = Backbone.View.extend({

	    className: 'job-comments',

		template: false,

		events: {
			'keypress #new-todo': 'createOnEnter'
		},

        initialize: function () {

		},

		render: function () {
			this.collection.each(function(comment) {
                var commentView = new CommentView({ model: comment });
                this.$el.append(commentView.render().el);
		    }, this);

    		return this;
		},

		addComment: function (todo) {
			var view = new TodoView({ model: todo });
			this.$todoList.append(view.render().el);
		},

		createOnEnter: function (e) {
			if (e.which !== 13 || !this.$input.val().trim()) {
				return;
			}

			Todos.create(this.newAttributes());
			this.$input.val('');
		}
	});

	return CommentsView;
});