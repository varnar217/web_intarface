//export { initCharts, addBer, addMer, addRxcsr, addRxst, addTxst, setSynch, setCrc32 };

Chart.defaults.global.legend.labels.boxWidth = 10;
Chart.defaults.global.legend.labels.padding = 5;
Chart.defaults.global.elements.point.pointStyle = 'rectRounded';
Chart.defaults.global.title.fontSize = 16;
Chart.defaults.global.title.fontFamily = 'consolas';
Chart.defaults.global.title.fontStyle = 'normal';
Chart.defaults.global.title.padding = 2;


let merconfig = {
    type: 'line',
    data: {
        labels: Array.from( {length:60 }, (v, k) => k),
        datasets: [{
            label: 'MER',
            backgroundColor: 'rgb(40, 167, 49, 0.5)',
            borderColor: 'rgba(40, 167, 49, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
            // pointStyle: 'circle',
            // radius: 10,
        },
        {
            label: 'RESNR',
            backgroundColor: 'rgba(255, 100, 0, 0.5)',
            borderColor: 'rgba(255, 100, 0, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
        },
        {
            label: 'FESNR',
            backgroundColor: 'rgba(255, 0, 100, 0.5)',
            borderColor: 'rgba(255, 0, 100, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
        },
        {
            label: 'FFSNR',
            backgroundColor: 'rgba(255, 100, 255, 0.5)',
            borderColor: 'rgba(255, 100, 255, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
        }]
    },
    options: {
        animation: {
                duration: 0 // general animation time
            },
        hover: {
            animationDuration: 0 // duration of animations when hovering an item
        },
        responsiveAnimationDuration: 0, // animation duration after a resize
        responsive: true,
        legend: {
            labels: {
                usePointStyle: true,
            }
        },
        maintainAspectRatio: false,
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        // hover: {
        //     mode: 'nearest',
        //     intersect: true
        // },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                },
                scaleLabel: {
                    display: true,
                    labelString: 'dB'
                }
                // type: 'logarithmic'
            }],
            // xAxes: [{
            //     scaleLabel: {
            //         display: true,
            //         labelString: 'sec'
            //     }
            // }],
        }
        // legend: {
        //     display: true,
        //     position: 'bottom',
        //     labels: {
        //         fontColor: '#333',
        //     }
        // }
    }
};
let berconfig = {
    type: 'line',
    data: {
        labels: Array.from( {length:60 }, (v, k) => k),
        datasets: [{
            label: 'BER',
            backgroundColor: 'rgba(255, 0, 0, 0.5)',
            borderColor: 'rgba(255, 0, 0, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
        }]
    },
    options: {
        animation: {
                duration: 0 // general animation time
            },
        hover: {
            animationDuration: 0 // duration of animations when hovering an item
        },
        responsiveAnimationDuration: 0, // animation duration after a resize
        responsive: true,
        legend: {
            labels: {
                usePointStyle: true,
            }
        },
        maintainAspectRatio: false,
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        // hover: {
        //     mode: 'nearest',
        //     intersect: true
        // },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                },
                type: 'logarithmic'
            }],
            // xAxes: [{
            //     scaleLabel: {
            //         display: true,
            //         labelString: 'sec'
            //     }
            // }],
        }
    }
};

let rxcsrconfig = {
    type: 'line',
    data: {
        labels: Array.from( {length:60 }, (v, k) => k),
        datasets: [{
            label: 'CSR',
            backgroundColor: 'rgba(0, 0, 255, 0.5)',
            borderColor: 'rgba(0, 0, 255, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
        },
        {
            label: 'CBW',
            backgroundColor: 'rgba(0, 255, 255, 0.5)',
            borderColor: 'rgba(0, 255, 255, 0.7)',
            fill: false,
            data: [], //Array.from(Array(60), ()=> 0),
            pointRadius: 0,
        }]
    },
    options: {
        animation: {
                duration: 0 // general animation time
            },
        hover: {
            animationDuration: 0 // duration of animations when hovering an item
        },
        responsiveAnimationDuration: 0, // animation duration after a resize
        responsive: true,
        legend: {
            labels: {
                usePointStyle: true,
            }
        },
        maintainAspectRatio: false,
        tooltips: {
            mode: 'nearest',
            intersect: false,
        },
        // hover: {
        //     mode: 'nearest',
        //     intersect: true
        // },
        scales: {
            yAxes: [{
                // ticks: {
                //     beginAtZero: true
                // },
                scaleLabel: {
                    display: true,
                    labelString: 'KSps'
                }
            }],
            // xAxes: [{
            //     scaleLabel: {
            //     display: true,
            //     labelString: 'sec'
            //     }
            // }],
        }
    }
};

// const dashMIR = [ 2, 2 ];
const dashCIR = [ 5, 5 ];
const thin = 1;
let stDatasets3 = [
    {
        label: 'CIR0',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(255, 0, 0, .5)',
        borderDash: dashCIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'DIR0',
        backgroundColor: 'rgba(255, 0, 0, .5)',
        borderColor: 'rgba(255, 0, 0, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'MIR0',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(255, 0, 0, .7)',
        // borderDash: dashMIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'CIR1',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(40, 167, 49, 0.7)',
        borderDash: dashCIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'DIR1',
        backgroundColor: 'rgba(40, 167, 49, 0.5)',
        borderColor: 'rgba(40, 167, 49, 0.7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'MIR1',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(40, 167, 49, 0.7)',
        // borderDash: dashMIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'CIR2',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(0, 0, 255, .5)',
        borderDash: dashCIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'DIR2',
        backgroundColor: 'rgba(0, 0, 255, .5)',
        borderColor: 'rgba(0, 0, 255, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'MIR2',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(0, 0, 255, .5)',
        // borderDash: dashMIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'CDR',
        backgroundColor: 'rgba(192, 192, 192, 0.5)',
        borderColor: 'rgba(192, 192, 192, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'CFR',
        backgroundColor: 'rgba(0, 255, 255, 0.5)',
        borderColor: 'rgba(0, 255, 255, 0.7)',
        // borderDash: [5],
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'CBR',
        backgroundColor: 'rgba(0, 0, 0, .5)',
        borderColor: 'rgba(0, 0, 0, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    }
]

let stDatasets2 = [
    {
        label: 'CIR0',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(255, 0, 0, .5)',
        borderDash: dashCIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'DIR0',
        backgroundColor: 'rgba(255, 0, 0, .5)',
        borderColor: 'rgba(255, 0, 0, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'MIR0',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(255, 0, 0, .7)',
        // borderDash: dashMIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'CIR1',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(40, 167, 49, 0.7)',
        borderDash: dashCIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'DIR1',
        backgroundColor: 'rgba(40, 167, 49, 0.5)',
        borderColor: 'rgba(40, 167, 49, 0.7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'MIR1',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(40, 167, 49, 0.7)',
        // borderDash: dashMIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'CDR',
        backgroundColor: 'rgba(192, 192, 192, 0.5)',
        borderColor: 'rgba(192, 192, 192, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'CFR',
        backgroundColor: 'rgba(0, 255, 255, 0.5)',
        borderColor: 'rgba(0, 255, 255, 0.7)',
        // borderDash: [5],
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'CBR',
        backgroundColor: 'rgba(0, 0, 0, .5)',
        borderColor: 'rgba(0, 0, 0, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    }
]

let stDatasets1 = [
    {
        label: 'CIR0',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(255, 0, 0, .5)',
        borderDash: dashCIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'DIR0',
        backgroundColor: 'rgba(255, 0, 0, .5)',
        borderColor: 'rgba(255, 0, 0, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'MIR0',
        backgroundColor: '#FFFFFF',
        borderColor: 'rgba(255, 0, 0, .7)',
        // borderDash: dashMIR,
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
        borderWidth: thin,
    },
    {
        label: 'CDR',
        backgroundColor: 'rgba(192, 192, 192, 0.5)',
        borderColor: 'rgba(192, 192, 192, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'CFR',
        backgroundColor: 'rgba(0, 255, 255, 0.5)',
        borderColor: 'rgba(0, 255, 255, 0.7)',
        // borderDash: [5],
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    },
    {
        label: 'CBR',
        backgroundColor: 'rgba(0, 0, 0, .5)',
        borderColor: 'rgba(0, 0, 0, .7)',
        fill: false,
        data: [], //Array.from(Array(60), ()=> 0),
        pointRadius: 0,
    }
]

let stconfig = {
    type: 'line',
    data: {
        labels: Array.from( {length:60 }, (v, k) => k),
        datasets: JSON.parse(JSON.stringify(stDatasets3))
    },
    options: {
        // title: {
        //     display: true,
        //     text: 'Приём (RX)'
        // },
        animation: {
                duration: 0 // general animation time
            },
        hover: {
            animationDuration: 0 // duration of animations when hovering an item
        },
        responsiveAnimationDuration: 0, // animation duration after a resize
        responsive: true,
        legend: {
            labels: {
                usePointStyle: true,
            }
        },
        maintainAspectRatio: false,
        tooltips: {
            mode: 'nearest',
            intersect: false,
        },
        // hover: {
        //     mode: 'nearest',
        //     intersect: true
        // },
        scales: {
            yAxes: [{
                // ticks: {
                //     beginAtZero: true
                // },
                scaleLabel: {
                    display: true,
                    labelString: 'Kbps'
                }
            }],
            // xAxes: [{
            //     scaleLabel: {
            //     display: true,
            //     labelString: 'sec'
            //     }
            // }],
        }
    }
};

// var setTXConfig = function(dataset)
// {
//         const txstconfig = {
//         type: 'line',
//         data: {
//             labels: Array.from( {length:60 }, (v, k) => k),
//             datasets: JSON.parse(JSON.stringify(dataset))
//         },
//         options: {
//             // title: {
//             //     display: true,
//             //     text: 'Приём (RX)'
//             // },
//             animation: {
//                     duration: 0 // general animation time
//                 },
//             hover: {
//                 animationDuration: 0 // duration of animations when hovering an item
//             },
//             responsiveAnimationDuration: 0, // animation duration after a resize
//             responsive: true,
//             legend: {
//                 labels: {
//                     usePointStyle: true,
//                 }
//             },
//             maintainAspectRatio: false,
//             tooltips: {
//                 mode: 'nearest',
//                 intersect: false,
//             },
//             // hover: {
//             //     mode: 'nearest',
//             //     intersect: true
//             // },
//             scales: {
//                 yAxes: [{
//                     // ticks: {
//                     //     beginAtZero: true
//                     // },
//                     scaleLabel: {
//                         display: true,
//                         labelString: 'Kbps'
//                     }
//                 }],
//                 // xAxes: [{
//                 //     scaleLabel: {
//                 //     display: true,
//                 //     labelString: 'sec'
//                 //     }
//                 // }],
//             }
//         }
//     };
//     return txstconfig;
// }

// var txstconfig = setTXConfig(stDatasets3);
// window.onload = function() {
//             var ber = document.getElementById('berChart').getContext('2d');
//             window.berLine = new Chart(ber, config);

//             var mer = document.getElementById('berChart').getContext('2d');
//             window.merLine = new Chart(mer, config);

//         };

let berChart = Array(4);
let merChart = Array(4);
let rxcsrChart = Array(4);
let rxstChart = Array(4);
let txstChart = Array(4);

var initCharts = function() {
	
	berChart[0] = new Chart(document.getElementById('chart-ber0'), JSON.parse(JSON.stringify(berconfig)));
	berChart[1] = new Chart(document.getElementById('chart-ber1'), JSON.parse(JSON.stringify(berconfig)));
	berChart[2] = new Chart(document.getElementById('chart-ber2'), JSON.parse(JSON.stringify(berconfig)));
	berChart[3] = new Chart(document.getElementById('chart-ber3'), JSON.parse(JSON.stringify(berconfig)));

	merChart[0] = new Chart(document.getElementById('chart-mer0'), JSON.parse(JSON.stringify(merconfig)));
	merChart[0].data.datasets[1].hidden = true;
	merChart[0].data.datasets[2].hidden = true;
	merChart[0].data.datasets[3].hidden = true;

	merChart[1] = new Chart(document.getElementById('chart-mer1'), JSON.parse(JSON.stringify(merconfig)));
	merChart[1].data.datasets[1].hidden = true;
	merChart[1].data.datasets[2].hidden = true;
	merChart[1].data.datasets[3].hidden = true;

	merChart[2] = new Chart(document.getElementById('chart-mer2'), JSON.parse(JSON.stringify(merconfig)));
	merChart[2].data.datasets[1].hidden = true;
	merChart[2].data.datasets[2].hidden = true;
	merChart[2].data.datasets[3].hidden = true;

	merChart[3] = new Chart(document.getElementById('chart-mer3'), JSON.parse(JSON.stringify(merconfig)));
	merChart[3].data.datasets[1].hidden = true;
	merChart[3].data.datasets[2].hidden = true;
	merChart[3].data.datasets[3].hidden = true;

	rxcsrChart[0] = new Chart(document.getElementById('chart-rxcsr0'), JSON.parse(JSON.stringify(rxcsrconfig)));
	rxcsrChart[1] = new Chart(document.getElementById('chart-rxcsr1'), JSON.parse(JSON.stringify(rxcsrconfig)));
	rxcsrChart[2] = new Chart(document.getElementById('chart-rxcsr2'), JSON.parse(JSON.stringify(rxcsrconfig)));
	rxcsrChart[3] = new Chart(document.getElementById('chart-rxcsr3'), JSON.parse(JSON.stringify(rxcsrconfig)));


	rxstChart[0] = new Chart(document.getElementById('chart-rxst0'), JSON.parse(JSON.stringify(stconfig)));
	rxstChart[1] = new Chart(document.getElementById('chart-rxst1'), JSON.parse(JSON.stringify(stconfig)));
	rxstChart[2] = new Chart(document.getElementById('chart-rxst2'), JSON.parse(JSON.stringify(stconfig)));
	rxstChart[3] = new Chart(document.getElementById('chart-rxst3'), JSON.parse(JSON.stringify(stconfig)));

	txstChart[0] = new Chart(document.getElementById('chart-txst0'), JSON.parse(JSON.stringify(stconfig)));
	txstChart[1] = new Chart(document.getElementById('chart-txst1'), JSON.parse(JSON.stringify(stconfig)));
	txstChart[2] = new Chart(document.getElementById('chart-txst2'), JSON.parse(JSON.stringify(stconfig)));
	txstChart[3] = new Chart(document.getElementById('chart-txst3'), JSON.parse(JSON.stringify(stconfig)));
}
// ctx.canvas.parentNode.style.height = '100px';
// ctx.canvas.parentNode.style.width = '100px';
Chart.defaults.global.defaultFontFamily = 'consolas';
Chart.defaults.global.defaultFontColor = 'rgba(0,0,0,.7)';
const number = 60;

var addBer = function(ch, ber)
{
    document.getElementById('output_ber'+ch).value = ber;
    // let n = berChart.data.labels.length
    // let v = berChart.data.labels[n-1] +1;
    // berChart.data.labels.pop()
    // berChart.data.labels.unshift(++number);
    if(berChart[ch].data.datasets[0].data.length == 60)
        berChart[ch].data.datasets[0].data.pop();
    berChart[ch].data.datasets[0].data.unshift(ber);
    berChart[ch].update();
}

var addMer = function(ch, mer, re, fe, ff)
{
    document.getElementById('output_mer'+ch).value = mer + " dB";
    if(merChart[ch].data.datasets[0].data.length == 60)
    {
        merChart[ch].data.datasets[0].data.pop();
        merChart[ch].data.datasets[1].data.pop();
        merChart[ch].data.datasets[2].data.pop();
        merChart[ch].data.datasets[3].data.pop();
    }
    merChart[ch].data.datasets[0].data.unshift(mer);
    merChart[ch].data.datasets[1].data.unshift(re);
    merChart[ch].data.datasets[2].data.unshift(fe);
    merChart[ch].data.datasets[3].data.unshift(ff);
    merChart[ch].update();
}

var addRxcsr = function(ch, csr, bn)
{
    let c = document.getElementById('output_rx_csr'+ch);

    csr = parseFloat(csr/1000).toFixed(1);
    bn = parseFloat(bn/1000).toFixed(1);

    c.value = csr  + " KSps";
    if (rxcsrChart[ch].data.datasets[0].data.length == 60)
    {
        rxcsrChart[ch].data.datasets[0].data.pop();
        rxcsrChart[ch].data.datasets[1].data.pop();
    }
    rxcsrChart[ch].data.datasets[0].data.unshift(csr);
    rxcsrChart[ch].data.datasets[1].data.unshift(bn);
    rxcsrChart[ch].update();
}

var addRxst = function(ch, streams, cir, dir, mir, cdr, cfr, cbr)
{
    //const streams = 1;
    cir.forEach((currentValue, index, array) => { array[index] = (currentValue/1024).toFixed(1) });
    mir.forEach((currentValue, index, array) => { array[index] = (currentValue/1024).toFixed(1) });
    dir.forEach((currentValue, index, array) => { array[index] = (currentValue/1024).toFixed(1) });
    cdr = (cdr/1024).toFixed(1);
    cfr = (cfr/1024).toFixed(1);
    cbr = (cbr/1024).toFixed(1);

    $('#output_rxdir'+ch+0).val(dir[0] + " Kbps");
    $('#output_rxdir'+ch+1).val(dir[1] + " Kbps");
    $('#output_rxdir'+ch+2).val(dir[2] + " Kbps");
    $('#output_rxcfr'+ch).val(cfr + " Kbps");
    $('#output_rxcdr'+ch).val(cdr + " Kbps");

    // let cdr0 = dir0;
    // let cdr1 = Number(dir0)+Number(dir1);
    // let cdr2 = Number(dir0)+Number(dir1)+Number(dir2);
    // let cdr3 = Number(dir0)+Number(dir1)+Number(dir2)+Number(cfr);

    if(rxstChart[ch].data.datasets[1].data.length == 60)
        rxstChart[ch].data.datasets.forEach( element => element.data.pop() );

    switch(streams) {
        case 3:
            if(rxstChart[ch].data.datasets.length !== 12) {
                rxstChart[ch].data.datasets = JSON.parse(JSON.stringify(stDatasets3));
                console.log("ch"+ch+" rxstreams set to 3");
            }
            rxstChart[ch].data.datasets[0].data.unshift(cir[0]);
            rxstChart[ch].data.datasets[1].data.unshift(dir[0]);
            rxstChart[ch].data.datasets[2].data.unshift(mir[0]);
            rxstChart[ch].data.datasets[3].data.unshift(cir[1]);
            rxstChart[ch].data.datasets[4].data.unshift(dir[1]);
            rxstChart[ch].data.datasets[5].data.unshift(mir[1]);
            rxstChart[ch].data.datasets[6].data.unshift(cir[2]);
            rxstChart[ch].data.datasets[7].data.unshift(dir[2]);
            rxstChart[ch].data.datasets[8].data.unshift(mir[2]);
            rxstChart[ch].data.datasets[9].data.unshift(cdr);
            rxstChart[ch].data.datasets[10].data.unshift(cfr);
            rxstChart[ch].data.datasets[11].data.unshift(cbr);
            break;
        case 2:
            if(rxstChart[ch].data.datasets.length !== 9) {
                rxstChart[ch].data.datasets = JSON.parse(JSON.stringify(stDatasets2));
                console.log("ch"+ch+" rxstreams set to 2");
            }
            rxstChart[ch].data.datasets[0].data.unshift(cir[0]);
            rxstChart[ch].data.datasets[1].data.unshift(dir[0]);
            rxstChart[ch].data.datasets[2].data.unshift(mir[0]);
            rxstChart[ch].data.datasets[3].data.unshift(cir[1]);
            rxstChart[ch].data.datasets[4].data.unshift(dir[1]);
            rxstChart[ch].data.datasets[5].data.unshift(mir[1]);
            rxstChart[ch].data.datasets[6].data.unshift(cdr);
            rxstChart[ch].data.datasets[7].data.unshift(cfr);
            rxstChart[ch].data.datasets[8].data.unshift(cbr);
            break;
        case 1:
            if(rxstChart[ch].data.datasets.length !== 6) {
                rxstChart[ch].data.datasets = JSON.parse(JSON.stringify(stDatasets1));
                console.log("ch"+ch+" rxstreams set to 1");
            }
            rxstChart[ch].data.datasets[0].data.unshift(cir[0]);
            rxstChart[ch].data.datasets[1].data.unshift(dir[0]);
            rxstChart[ch].data.datasets[2].data.unshift(mir[0]);
            rxstChart[ch].data.datasets[3].data.unshift(cdr);
            rxstChart[ch].data.datasets[4].data.unshift(cfr);
            rxstChart[ch].data.datasets[5].data.unshift(cbr);
            break;
        default:
            rxstChart[ch].data.datasets[0].data.unshift(cir[0]);
            rxstChart[ch].data.datasets[1].data.unshift(dir[0]);
            rxstChart[ch].data.datasets[2].data.unshift(mir[0]);
            rxstChart[ch].data.datasets[3].data.unshift(cir[1]);
            rxstChart[ch].data.datasets[4].data.unshift(dir[1]);
            rxstChart[ch].data.datasets[5].data.unshift(mir[1]);
            rxstChart[ch].data.datasets[6].data.unshift(cir[2]);
            rxstChart[ch].data.datasets[7].data.unshift(dir[2]);
            rxstChart[ch].data.datasets[8].data.unshift(mir[2]);
            rxstChart[ch].data.datasets[9].data.unshift(cdr);
            rxstChart[ch].data.datasets[10].data.unshift(cfr);
            rxstChart[ch].data.datasets[11].data.unshift(cbr);
    }
    rxstChart[ch].update();
}

var addTxst = function(ch, streams, cir, dir, mir, cdr, cfr, cbr)
{
    //const streams = 2;
    cir.forEach((currentValue, index, array) => { array[index] = (currentValue/1024).toFixed(1) });
    mir.forEach((currentValue, index, array) => { array[index] = (currentValue/1024).toFixed(1) });
    dir.forEach((currentValue, index, array) => { array[index] = (currentValue/1024).toFixed(1) });
    cdr = (cdr/1024).toFixed(1);
    cfr = (cfr/1024).toFixed(1);
    cbr = (cbr/1024).toFixed(1);

    $('#output_txdir'+ch+0).val(dir[0] + " Kbps");
    $('#output_txdir'+ch+1).val(dir[1] + " Kbps");
    $('#output_txdir'+ch+2).val(dir[2] + " Kbps");
    $('#output_txcfr'+ch).val(cfr + " Kbps");
    $('#output_txcdr'+ch).val(cdr + " Kbps");

    // let cdr0 = dir0;
    // let cdr1 = Number(dir0)+Number(dir1);
    // let cdr2 = Number(dir0)+Number(dir1)+Number(dir2);
    // let cdr3 = Number(dir0)+Number(dir1)+Number(dir2)+Number(cfr);

    if(txstChart[ch].data.datasets[0].data.length == 60)
        txstChart[ch].data.datasets.forEach( element => element.data.pop() );

    switch(streams) {
        case 3:
            if(txstChart[ch].data.datasets.length !== 12) {
                txstChart[ch].data.datasets = JSON.parse(JSON.stringify(stDatasets3));
                console.log("ch"+ch+" txstreams set to 3");
            }
            txstChart[ch].data.datasets[0].data.unshift(cir[0]);
            txstChart[ch].data.datasets[1].data.unshift(dir[0]);
            txstChart[ch].data.datasets[2].data.unshift(mir[0]);
            txstChart[ch].data.datasets[3].data.unshift(cir[1]);
            txstChart[ch].data.datasets[4].data.unshift(dir[1]);
            txstChart[ch].data.datasets[5].data.unshift(mir[1]);
            txstChart[ch].data.datasets[6].data.unshift(cir[2]);
            txstChart[ch].data.datasets[7].data.unshift(dir[2]);
            txstChart[ch].data.datasets[8].data.unshift(mir[2]);
            txstChart[ch].data.datasets[9].data.unshift(cdr);
            txstChart[ch].data.datasets[10].data.unshift(cfr);
            txstChart[ch].data.datasets[11].data.unshift(cbr);
            break;
        case 2:
            if(txstChart[ch].data.datasets.length !== 9) {
                txstChart[ch].data.datasets = JSON.parse(JSON.stringify(stDatasets2));
                console.log("ch"+ch+" txstreams set to 2");
            }
            txstChart[ch].data.datasets[0].data.unshift(cir[0]);
            txstChart[ch].data.datasets[1].data.unshift(dir[0]);
            txstChart[ch].data.datasets[2].data.unshift(mir[0]);
            txstChart[ch].data.datasets[3].data.unshift(cir[1]);
            txstChart[ch].data.datasets[4].data.unshift(dir[1]);
            txstChart[ch].data.datasets[5].data.unshift(mir[1]);
            txstChart[ch].data.datasets[6].data.unshift(cdr);
            txstChart[ch].data.datasets[7].data.unshift(cfr);
            txstChart[ch].data.datasets[8].data.unshift(cbr);
            break;
        case 1:
            if(txstChart[ch].data.datasets.length !== 6) {
                txstChart[ch].data.datasets = JSON.parse(JSON.stringify(stDatasets1));
                console.log("ch"+ch+" txstreams set to 1");
            }
            txstChart[ch].data.datasets[0].data.unshift(cir[0]);
            txstChart[ch].data.datasets[1].data.unshift(dir[0]);
            txstChart[ch].data.datasets[2].data.unshift(mir[0]);
            txstChart[ch].data.datasets[3].data.unshift(cdr);
            txstChart[ch].data.datasets[4].data.unshift(cfr);
            txstChart[ch].data.datasets[5].data.unshift(cbr);
            break;
        default:
            txstChart[ch].data.datasets[0].data.unshift(cir[0]);
            txstChart[ch].data.datasets[1].data.unshift(dir[0]);
            txstChart[ch].data.datasets[2].data.unshift(mir[0]);
            txstChart[ch].data.datasets[3].data.unshift(cir[1]);
            txstChart[ch].data.datasets[4].data.unshift(dir[1]);
            txstChart[ch].data.datasets[5].data.unshift(mir[1]);
            txstChart[ch].data.datasets[6].data.unshift(cir[2]);
            txstChart[ch].data.datasets[7].data.unshift(dir[2]);
            txstChart[ch].data.datasets[8].data.unshift(mir[2]);
            txstChart[ch].data.datasets[9].data.unshift(cdr);
            txstChart[ch].data.datasets[10].data.unshift(cfr);
            txstChart[ch].data.datasets[11].data.unshift(cbr);            
    }
    txstChart[ch].update();
}

var setSynch = function(ch, synch)
{
    if( synch )
    {
        $('a.led#led_synch_lock'+ch).addClass("led_green"); //.delay( 300 ).removeClass("led_green");
        $('a.led#led_synch_lock'+ch).css("background-color", "rgba(132, 244, 33, .8)");
        setTimeout(() => { $('a.led#led_synch_lock'+ch).removeClass("led_green"); }, 200);
    } else {
        $('a.led#led_synch_lock'+ch).addClass("led_red"); //.delay( 300 ).removeClass("led_green");
        $('a.led#led_synch_lock'+ch).css("background-color", "rgba(244, 77, 33, .7)");
        setTimeout(() => { $('a.led#led_synch_lock'+ch).removeClass("led_red"); }, 200);
    }
}

var setCrc32 = function(ch, crc32)
{
    if( crc32 )
    {
        $('a.led#led_crc32_check'+ch).addClass("led_red"); //.delay( 300 ).removeClass("led_green");
        $('a.led#led_crc32_check'+ch).css("background-color", "rgba(244, 77, 33, .7)");
        setTimeout(() => { $('a.led#led_crc32_check'+ch).removeClass("led_red"); }, 200);
    } else {

        $('a.led#led_crc32_check'+ch).addClass("led_green"); //.delay( 300 ).removeClass("led_green");
        $('a.led#led_crc32_check'+ch).css("background-color", "rgba(132, 244, 33, .8)");
        setTimeout(() => { $('a.led#led_crc32_check'+ch).removeClass("led_green"); }, 200);
    }
}
