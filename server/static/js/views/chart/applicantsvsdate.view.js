define(['lib/jquery', 'lib/underscore', 'lib/chartjs', 'lib/moment',
        'js/views/chart/chart.view'],
	function($, _, Chart, Moment, ChartView){

    var JobsVsTermsView = ChartView.extend({

        initialize: function(options) {
            options = options || {};
            options.data = options.data || {};

            options.data = {
                'card-icon': options.data.icon || 'fa fa-line-chart',
                'title': options.data.title || 'Applicants history'
            };

            ChartView.prototype.initialize.apply(this, [options]);
        },

        drawChart: function(){
            var ctx = this.$(".card-chart")[0];
            var self = this;

			Chart.defaults.global.fontFamily = '"Roboto", sans-serif';

            var applicants = _.sortBy(window.applicants, function(applicant){
                return applicant.date;
            });

            var labels = [];
            var data = [];

            _.each(applicants, function(applicant){
                labels.push(Moment(applicant.date).format('MMM Do, YYYY'));
                data.push(applicant.applicants);
            });

            setTimeout(function(){
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: "Applicants",
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
        },

        _getTermPriority: function(term){
            switch(term) {
                case 'Fall':
                    return 1;
                case 'Winter':
                    return 2;
                case 'Spring':
                    return 3;
                default:
                    return 0;
            }
        }

    });

    return JobsVsTermsView;

});