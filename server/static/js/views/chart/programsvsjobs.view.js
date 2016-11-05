define(['lib/jquery', 'lib/underscore', 'lib/chartjs',
        'js/views/chart/chart.view'],
	function($, _, Chart, ChartView){

    var ProgramsVsJobsView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-bar-chart',
                'title': options.data.title || 'Jobs vs. Programs'
            };

            ChartView.prototype.initialize.apply(this, [options]);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];

			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            $.post('/api/programs-vs-jobs-stat', '', function(response){
                var programs = _.sortBy(response.data, function(program){
                    return program.jobs;
                }).reverse();

                var labels = [];
                var data = [];

                _.each(programs, function(program){
                    if (labels.length <= 15){
                        labels.push(program.name);
                    }
                    if (data.length <= 15){
                        data.push(program.jobs)
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

    return ProgramsVsJobsView;

});