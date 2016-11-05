define(['lib/jquery', 'lib/chartjs', 'js/views/chart/chart.view'],
	function($, Chart, ChartView){

    var MostPopularProgramsView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-bar-chart',
                'title': options.data.title || 'Jobs vs. Programs'
            };

            ChartView.prototype.constructor(options);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];

            Chart.defaults.global.responsive = true;
			Chart.defaults.global.legend.display = true;
			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            setTimeout(function(){
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ["JAN", "FEB", "MAR", "APR", "MAY", "JUN"],
                        datasets: [{
                            label: 'Finished',
                            data: [310, 174, 254, 268, 324, 385],
                            backgroundColor: '#ff9800',
                            borderColor: '#ff9800',
                            borderWidth: 1,
                            pointRadius: 0,
                            pointHoverRadius: 5,
                            pointHoverBackgroundColor: '#2196F3',
                            pointHoverBorderWidth: 2,
                            pointHoverBorderColor: '#1976d2',
                            pointHitRadius: 10
                        }, {
                            label: 'Started',
                            data: [620, 251, 485, 598, 658, 652],
                            backgroundColor: '#ffe0b2',
                            borderColor: '#ffe0b2',
                            borderWidth: 1,
                            pointRadius: 0,
                            pointHoverRadius: 5,
                            pointHoverBackgroundColor: '#2196F3',
                            pointHoverBorderWidth: 2,
                            pointHoverBorderColor: '#1976d2',
                            pointHitRadius: 10
                        }]
                    },
                    options: {
                        scales: {
                            xAxes: [{
                                showLines: false
                            }],
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true
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

        }

    });

    return MostPopularProgramsView;

});