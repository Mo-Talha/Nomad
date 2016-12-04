require(['lib/jquery', 'lib/underscore', 'js/views/comments/comments.view',
        'js/collections/comments.collection', 'js/util',
        'js/search'],
    function($, _, CommentsView, CommentCollection, Util) {

    $('.navbar-menu').click(function(){
        $('.navbar-items').animate({height: 'toggle'}, 200);
    });

    var collection = [];

    if (window.comments && window.comments.length > 0){
        _.each(window.comments, function(comment){
            collection.push({
                text: comment.comment,
                date: comment.date,
                date_formatted: Util._convertToFormattedDate(comment.date),
                salary: comment.salary,
                rating: comment.rating,
                crawled: comment.crawled
            })
        });
    }

    $(document).ready(function(){
        var comments = new CommentsView({collection: new CommentCollection(collection)});
        comments.render();

        $('.job-container').append(comments.el);
    });
});