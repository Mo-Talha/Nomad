define(['lib/jquery', 'lib/underscore', 'lib/chartjs',
        'js/views/chart/chart.view'],
	function($, _, Chart, ChartView){

    var JobsVsJavaScriptLibrariesView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-bar-chart',
                'title': options.data.title || 'Most Popular JavaScript Libraries/Frameworks'
            };

            ChartView.prototype.initialize.apply(this, [options]);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];

			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            $.post('/api/jobs-vs-js-libraries-stat', '', function(response){
                var libraries = _.sortBy(response.data, function(library){
                    return library.jobs;
                }).reverse();

                var labels = [];
                var data = [];

                _.each(libraries, function(library){
                    if (labels.length <= 15){
                        labels.push(library.name);
                    }
                    if (data.length <= 15){
                        data.push(library.jobs)
                    }
                });

                setTimeout(function(){
                    new Chart(ctx, {
                        type: 'horizontalBar',
                        data: {
                            labels: labels,
                            datasets: [{
                                data: data,
                                backgroundColor: '#ff9800',
                                borderColor: '#ff9800'
                            }]
                        },
                        options: {
                            legend: {
                                display: false
                            },
                            scales: {
                                xAxes: [{
                                    showLines: false,
                                    barPercentage: 0.0,
                                    ticks: {
                                        maxRotation: 0,
                                        minRotation: 0
                                    }
                                }]
                            },
                            animation: {
                                duration: 1000
                            },
                            responsive: true,
                            maintainAspectRatio: false
                        }
                    });
                }, 0);
            });
        }

    });

    return JobsVsJavaScriptLibrariesView;

});