define(['lib/backbone', 'hbs!js/views/chart/chart'],
    function (Backbone, template) {

	var ChartView = Backbone.View.extend({

        tagName: 'div',

		className:  'chart-container',

		template: template,

		initialize: function (options) {
            this.options = options || {};
		},

		render: function () {
   			this.$el.html(this.template(this.options.data));
            this.drawChart();
			return this;
		}

	});

	return ChartView;
});

