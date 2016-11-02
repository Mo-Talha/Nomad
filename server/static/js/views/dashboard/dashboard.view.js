define(['lib/backbone', 'lib/underscore', 'lib/jquery'],
    function(Backbone, _, $){

    var DashboardView = Backbone.View.extend({
        tagName: 'div',

        className: 'dashboard',

        template: false,

        initialize: function(options) {
            this.commentView = new CommentView({ model: this.model });
            this.ratingsView = new ratings.RatingChoiceCollectionView({
                collection: this.model.get('ratings'),
                readOnly: true
            });
        },

        events: {
            'click .review-btn': 'reviewButtonClicked'
        },

        reviewButtonClicked: function(e) {
            var yesBtnClicked = $(e.currentTarget).hasClass('yes-btn');
            var noBtnClicked = $(e.currentTarget).hasClass('no-btn');
            if (yesBtnClicked) {
                this.model.set('num_voted_helpful',
                this.model.get('num_voted_helpful') + 1);
            } else if (noBtnClicked) {
                this.model.set('num_voted_not_helpful',
                this.model.get('num_voted_not_helpful') + 1);
            }

            $.ajax('/api/v1/user/rate_review_for_user', {
                type: 'PUT',
                data: {
                    'review_id': this.model.get('user_course_id'),
                    'review_type': this.model.get('review_type'),
                'voted_helpful': yesBtnClicked
                }
            });

            this.model.set('can_vote', false);
            this.render();
        },

        render: function() {
            this.$el.html(this.template({}));
            this.$('.comment-placeholder').replaceWith(this.commentView.render().el);
            this.$('.ratings-placeholder').replaceWith(this.ratingsView.render().el);
            return this;
        }
    });


});