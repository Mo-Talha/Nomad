define(['lib/backbone', 'lib/underscore', 'js/models/chart'],
    function (Backbone, _, Chart) {

	var TodosCollection = Backbone.Collection.extend({
		model: Chart,

		comparator: 'order'
	});

	return new TodosCollection();
});