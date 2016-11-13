define(['lib/jquery', 'lib/underscore', 'lib/chartjs',
        'js/views/chart/chart.view'],
	function($, _, Chart, ChartView){

    var JobsVsLevelsView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-pie-chart',
                'title': options.data.title || 'Most Popular OSs'
            };

            ChartView.prototype.initialize.apply(this, [options]);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];

			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            $.post('/api/jobs-vs-operating-systems-stat', '', function(response){
                var oses = _.sortBy(response.data, function(os){
                    return os.jobs;
                }).reverse();

                var labels = [];
                var data = [];

                _.each(oses, function(os){
                    if (labels.length <= 10){
                        labels.push(os.name);
                    }
                    if (data.length <= 10){
                        data.push(os.jobs)
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
                                    "#FF6384",
                                    "#36A2EB",
                                    "#FFCE56",
                                    "#F7464A",
                                    "#46BFBD",
                                    "rgba(75,192,192,0.4)",
                                    "#196c32",
                                    "#FDB45C",
                                    "#949FB1",
                                    "#4D5360"
                                ],
                                hoverBackgroundColor: [
                                    "#FF6384",
                                    "#36A2EB",
                                    "#FFCE56",
                                    "#F7464A",
                                    "#46BFBD",
                                    "rgba(75,192,192,0.4)",
                                    "#196c32",
                                    "#FDB45C",
                                    "#949FB1",
                                    "#4D5360"
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