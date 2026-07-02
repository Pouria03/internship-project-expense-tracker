document.addEventListener('DOMContentLoaded', function () {
    'use strict';

    var dataEl = document.getElementById('chart-data');
    if (!dataEl) return;

    var chartData = JSON.parse(dataEl.textContent);

    var glassColors = [
        'rgba(108, 92, 231, 0.8)',
        'rgba(0, 206, 201, 0.8)',
        'rgba(253, 203, 110, 0.8)',
        'rgba(253, 121, 168, 0.8)',
        'rgba(85, 239, 196, 0.8)',
        'rgba(116, 185, 255, 0.8)'
    ];

    var glassBorder = [
        'rgba(108, 92, 231, 1)',
        'rgba(0, 206, 201, 1)',
        'rgba(253, 203, 110, 1)',
        'rgba(253, 121, 168, 1)',
        'rgba(85, 239, 196, 1)',
        'rgba(116, 185, 255, 1)'
    ];

    function createChart(id, config) {
        var ctx = document.getElementById(id);
        if (!ctx) return;
        return new Chart(ctx, config);
    }

    createChart('categoryChart', {
        type: 'doughnut',
        data: {
            labels: chartData.category_labels,
            datasets: [{
                data: chartData.category_data,
                backgroundColor: glassColors,
                borderColor: glassBorder,
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: 'rgba(255,255,255,0.7)', font: { family: 'Vazirmatn' } }
                }
            }
        }
    });

    createChart('monthlyChart', {
        type: 'bar',
        data: {
            labels: chartData.monthly_labels,
            datasets: [{
                label: 'هزینه (تومان)',
                data: chartData.monthly_data,
                backgroundColor: 'rgba(0, 206, 201, 0.6)',
                borderColor: 'rgba(0, 206, 201, 1)',
                borderWidth: 2,
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: 'rgba(255,255,255,0.7)', font: { family: 'Vazirmatn' } }
                }
            },
            scales: {
                x: {
                    ticks: { color: 'rgba(255,255,255,0.5)', font: { family: 'Vazirmatn' } },
                    grid: { color: 'rgba(255,255,255,0.05)' }
                },
                y: {
                    ticks: { color: 'rgba(255,255,255,0.5)', font: { family: 'Vazirmatn' } },
                    grid: { color: 'rgba(255,255,255,0.05)' }
                }
            }
        }
    });

    createChart('evalChart', {
        type: 'doughnut',
        data: {
            labels: chartData.evaluation_labels,
            datasets: [{
                data: chartData.evaluation_data,
                backgroundColor: glassColors.slice(0, chartData.evaluation_data.length),
                borderColor: glassBorder.slice(0, chartData.evaluation_data.length),
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: 'rgba(255,255,255,0.7)', font: { family: 'Vazirmatn' } }
                }
            }
        }
    });
});
