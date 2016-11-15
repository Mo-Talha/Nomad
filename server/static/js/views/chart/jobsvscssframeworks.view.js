define(['lib/jquery', 'lib/underscore', 'lib/chartjs',
        'js/views/chart/chart.view'],
	function($, _, Chart, ChartView){

    var JobsVsLevelsView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-pie-chart',
                'title': options.data.title || 'Most Popular CSS Frameworks'
            };

            ChartView.prototype.initialize.apply(this, [options]);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];

			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            $.post('/api/jobs-vs-css-frameworks-stat', '', function(response){
                var frameworks = _.sortBy(response.data, function(framework){
                    return framework.jobs;
                }).reverse();

                var labels = [];
                var data = [];

                _.each(frameworks, function(framework){
                    if (labels.length <= 10){
                        labels.push(framework.name);
                    }
                    if (data.length <= 10){
                        data.push(framework.jobs)
                    }
                });

                setTimeout(function(){
                    new Chart(ctx, {
                        type: 'doughnut',
                        data: {
                            labels: labels,
                            datasets: [{
                                data: data,
                                backgroundColor: [
                                    "#F7464A",
                                    "#46BFBD",
                                    "#FDB45C",
                                    "#949FB1",
                                    "#4D5360",
                                    "#669999",
                                    "#FF6384",
                                    "#36A2EB",
                                    "#fbbc05",
                                    "#196c32"
                                ],
                                hoverBackgroundColor: [
                                    "#F7464A",
                                    "#46BFBD",
                                    "#FDB45C",
                                    "#949FB1",
                                    "#4D5360",
                                    "#669999",
                                    "#FF6384",
                                    "#36A2EB",
                                    "#fbbc05",
                                    "#196c32"
                                ]
                            }]
                        },
                        options: {
                            legend: {
                                display: true
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

    return JobsVsLevelsView;

});