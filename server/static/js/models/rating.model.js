define(['lib/backbone'], function(Backbone) {

    var Rating = Backbone.Model.extend({
        defaults: function() {
            return {
                rating: 0,
                ratings: ['fa-star-o', 'fa-star-o', 'fa-star-o', 'fa-star-o', 'fa-star-o']
            };
        }

    });

    return Rating;
});
