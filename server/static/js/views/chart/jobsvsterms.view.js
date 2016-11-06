define(['lib/jquery', 'lib/underscore', 'lib/chartjs',
        'js/views/chart/chart.view'],
	function($, _, Chart, ChartView){

    var ProgramsVsJobsView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-line-chart',
                'title': options.data.title || 'Jobs vs. Term'
            };

            ChartView.prototype.initialize.apply(this, [options]);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];

			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            $.post('/api/jobs-vs-terms-stat', '', function(response){
                var terms = _.sortBy(response.data, function(term){
                    return term.year;
                });

                var labels = [];
                var data = [];

                _.each(terms, function(term){
                    labels.push(term.term + ' ' + term.year);
                    data.push(term.jobs);
                });

                setTimeout(function(){
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: labels,
                            datasets: [{
                                label: "Jobs",
                                fill: true,
                                lineTension: 0.2,
                                backgroundColor: "rgba(75,192,192,0.4)",
                                borderColor: "rgba(75,192,192,1)",
                                borderCapStyle: 'butt',
                                borderDash: [],
                                borderDashOffset: 0.0,
                                borderJoinStyle: 'miter',
                                pointBorderColor: "rgba(75,192,192,1)",
                                pointBackgroundColor: "#fff",
                                pointBorderWidth: 1,
                                pointHoverRadius: 5,
                                pointHoverBackgroundColor: "rgba(75,192,192,1)",
                                pointHoverBorderColor: "rgba(220,220,220,1)",
                                pointHoverBorderWidth: 2,
                                pointRadius: 1,
                                pointHitRadius: 10,
                                data: data,
                                spanGaps: false
                            }]
                        },
                        options: {
                            scales: {
                                xAxes: [{
                                    gridLines: {
                                        display: true
                                    },
                                    showLines: true
                                }],
                                yAxes: [{
                                    gridLines: {
                                        display: true
                                    },
                                    showLines: true
                                }]
                            },
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

    return ProgramsVsJobsView;

});