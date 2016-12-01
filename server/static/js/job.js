require(['lib/jquery', 'lib/underscore', 'js/views/comments/comments.view',
        'js/collections/comments.collection', 'js/util',
        'js/search'],
    function($, _, CommentsView, CommentCollection, Util) {

    $('.navbar-menu').click(function(){
        $('.navbar-items').animate({height: 'toggle'}, 200);
    });

    var collection = [];

    if (window.comments && window.comments.length > 0){
        collection = new CommentCollection(_.map(window.comments,
            function(comment){
            return {
                text: comment.comment,
                date: comment.date,
                date_formatted: Util._convertToFormattedDate(comment.date),
                salary: comment.salary,
                rating: comment.rating,
                crawled: comment.crawled
            };
        }));

        var comments = new CommentsView({collection: collection});
        comments.render();

        $('.job-container').append(comments.el);
    }
});