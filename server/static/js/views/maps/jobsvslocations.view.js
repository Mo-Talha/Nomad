define(['lib/jquery',
        'lib/underscore',
        'js/views/maps/map.view',
        'async!https://maps.googleapis.com/maps/api/js?key=AIzaSyBcJygIpnxZSRZ4XguFT8w-M586hCNx30g'],
	function($, _, MapView){

    var JobsVsLocationsView = MapView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-globe',
                'title': options.data.title || 'Jobs vs. Locations'
            };

            MapView.prototype.initialize.apply(this, [options]);
        },

        drawMap: function(){
            var cardMap = this.$('.card-body').get(0);

            $.post('/api/jobs-vs-locations-stat', '', function(response){
                var locations = response.data;

                setTimeout(function(){
                    var map = new google.maps.Map(cardMap, {
                        zoom: 1,
                        center: {
                            lat: 0,
                            lng: 0
                        }
                    });

                    _.each(locations, function(location){
                        new google.maps.Marker({
                          position: {
                              lat: location.longitude,
                              lng: location.longitude
                          },
                          map: map,
                          title: location.name || 'Location not found'
                        });
                    });
                }, 0);
            });
        }

    });

    return JobsVsLocationsView;

});