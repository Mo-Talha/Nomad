define(['lib/jquery', 'lib/backbone'], function($, Backbone) {

    var Comment = Backbone.Model.extend({
        defaults: function() {
            return {
                id: window.job_id,
                text: 'N/A',
                date: new Date(),
                date_formatted: new Date(),
                salary: 'N/A',
                rating: 0,
                crawled: false
            };
        }

    });

    return Comment;
});
