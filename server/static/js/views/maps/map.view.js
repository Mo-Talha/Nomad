define(['lib/backbone', 'hbs!js/views/maps/map'],
    function (Backbone, template) {

	var MapView = Backbone.View.extend({

        tagName: 'div',

		className:  'map-container',

		template: template,

		initialize: function (options) {
            this.options = options || {};
		},

		render: function () {
   			this.$el.html(this.template(this.options.data));
            this.drawMap();
			return this;
		}

	});

	return MapView;
});

