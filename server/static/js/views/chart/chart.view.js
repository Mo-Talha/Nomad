define(['lib/backbone', 'hbs!js/views/chart/chart'],
    function (Backbone, template) {

	var ChartView = Backbone.View.extend({

		tagName:  'chart-container',

		template: template,

		initialize: function () {
			this.listenTo(this.model, 'change', this.render);
			this.listenTo(this.model, 'destroy', this.remove);
		},

		render: function () {
   			this.$el.html(this.template(this.model.toJSON()));
            this.drawChart();
			return this;
		}
	});

	return ChartView;
});

