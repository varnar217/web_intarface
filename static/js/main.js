//import { initCharts, addBer, addMer, addRxcsr, addRxst, addTxst, setSynch, setCrc32 } from './stchart.js';

$(document).ready(function() {
    initCharts();

    var gstatus = "HUBOFF";
    setInterval(function ()
    {
        let stat= $("#output_status");
        let connect= $("#output_connect");
        $.ajax({
            type: "POST",
            url: mldrCheck(),
            data: { request:$.toJSON({"command":"STATUS"}), ip: lhs_ip },
            timeout: 2000,
        })
        .done(function(data) {
          // let response = JSON.parse(data); //JSON.stringify(data);
          if( gstatus !== data )
          {
              gstatus = data;
              log(msg, "Статус обновлен: "+data);
          }
          switch(gstatus) {
            case "IDLE":
                //reset(true);
                stat.val("в ожидании");
                connect.val("в сети");
              break;
            case "ON_AIR":
                //reset(false);
                stat.val("работает");
                connect.val("в сети");
                break;
            case "READY":
                //reset(true);
                //toZero();
                stat.val("готов");
                connect.val("в сети");
                break;
            case "timeout": //есть соединение, но модем не высылает свой статус более 10 секунд
                //toZero();
                stat.val("недоступен");
                connect.val("в сети");
                break;
            case "MODOFF":
                //toZero();
                stat.val("недоступен");
                connect.val("модем недоступен");
                break;
            case "HUBOFF":
                //toZero();
                stat.val("недоступен");
                connect.val("локальный хаб недоступен");
                break;
            case "DBOFF":
                //toZero();
                stat.val("недоступен");
                connect.val("база данных недоступна");
                break;
            case "MLDROFF":
                //toZero();
                stat.val("недоступен");
                connect.val("защищенный канал недоступен");
                break;
            default:
                //toZero();
                stat.val("недоступен");
                connect.val("недоступен");
                console.log(gstatus);
          }
        })
        .fail(function() {
            //toZero();
            stat.val("недоступен");
            connect.val("сервер недоступен");
            //alert( "Error to request status.php" );
        })
    }, 1000);

    // периодический запрос статистики у базы данных
    // setInterval(function ()
    // {
    //     if( gstatus == "ON_AIR" || gstatus == "IDLE") {
    //         $.ajax({
    //             type: "POST",
    //             url: "pdo_mysql.php", //
    //             timeout: 300,
    //          })
    //         .done(function(data) {
    //             const now_m = new Date().format("yyyy-MM-dd HH:mm:ss fff");
    //             let statJSON = JSON.parse(data); //JSON.stringify(data);
    //             let err = statJSON.error;
    //             if(err) {
    //                 if(err == 2002)
    //                 {
    //                     log(msg, "Ответ DATABASE OFFLINE");
    //                 }
    //                 else log(msg, "Ответ DATABASE: "+statJSON.message);
    //             }
    //             else {
    //                 //log(msg, "Ответ DATABASE: BER "+statJSON.ber+" MER "+statJSON.mer);
    //                 ber.val(statJSON.ber);
    //                 mer.val(statJSON.mer);
    //             }
    //         })
    //         .fail(function() {
    //             console.log( "error: fail to get data from database" );
    //         })
    //     }
    // }, 1000);

    // периодический запрос статистики у LHS
    setInterval(function ()
    {
        if( gstatus == "ON_AIR" || gstatus == "IDLE") {
            $.ajax({
                type: "POST",
                url: mldrCheck(), //
                data: { request:$.toJSON({"command":"GET_STATISTIC"}), ip: lhs_ip() },
                timeout: 2000,
             })
            .done(function(data) {
                // const now_m = new Date().format("yyyy-MM-dd HH:mm:ss fff");
                //log(msg, "Ответ "+ data);
                //console.log(data);
                const statJSON = JSON.parse(data); //JSON.stringify(data);
                const uch_count = parseInt(statJSON[0].uch_count, 10);
                const dch_count = parseInt(statJSON[0].dch_count, 10);
                let ch_count;
                uch_count >= dch_count ? ch_count =  uch_count : ch_count = dch_count;
                for(let i = 0; i < 4; i++)
                {
                    if(ch_count !== 0 ) {
                        document.getElementById('nav-ch'+i+'-tab').innerHTML = "Канал "+(Number(i)+Number(1));
                        ch_count--;
                    }
                    else
                        document.getElementById('nav-ch'+i+'-tab').innerHTML = "";
                }

                addBer(0, parseFloat(statJSON[1].ber).toExponential(2));
                addBer(1, parseFloat(statJSON[2].ber).toExponential(2));
                addBer(2, parseFloat(statJSON[3].ber).toExponential(2));
                addBer(3, parseFloat(statJSON[4].ber).toExponential(2));

                addMer(0, parseFloat(statJSON[1].mer).toFixed(1),
                          parseFloat(statJSON[1].resnr).toFixed(1),
                          parseFloat(statJSON[1].fesnr).toFixed(1),
                          parseFloat(statJSON[1].ffsnr).toFixed(1));
                addMer(1, parseFloat(statJSON[2].mer).toFixed(1),
                          parseFloat(statJSON[2].resnr).toFixed(1),
                          parseFloat(statJSON[2].fesnr).toFixed(1),
                          parseFloat(statJSON[2].ffsnr).toFixed(1));
                addMer(2, parseFloat(statJSON[3].mer).toFixed(1),
                          parseFloat(statJSON[3].resnr).toFixed(1),
                          parseFloat(statJSON[3].fesnr).toFixed(1),
                          parseFloat(statJSON[3].ffsnr).toFixed(1));
                addMer(3, parseFloat(statJSON[4].mer).toFixed(1),
                          parseFloat(statJSON[4].resnr).toFixed(1),
                          parseFloat(statJSON[4].fesnr).toFixed(1),
                          parseFloat(statJSON[4].ffsnr).toFixed(1));

                addRxcsr(0, parseInt(statJSON[1].rx_csr, 10), parseInt(statJSON[1].rx_bandwidth, 10));
                addRxcsr(1, parseInt(statJSON[2].rx_csr, 10), parseInt(statJSON[2].rx_bandwidth, 10));
                addRxcsr(2, parseInt(statJSON[3].rx_csr, 10), parseInt(statJSON[3].rx_bandwidth, 10));
                addRxcsr(3, parseInt(statJSON[4].rx_csr, 10), parseInt(statJSON[4].rx_bandwidth, 10));

                setSynch(0, parseInt(statJSON[1].synch_lock, 10));
                setSynch(1, parseInt(statJSON[2].synch_lock, 10));
                setSynch(2, parseInt(statJSON[3].synch_lock, 10));
                setSynch(3, parseInt(statJSON[4].synch_lock, 10));

                setCrc32(0, parseInt(statJSON[1].crc32_check, 10));
                setCrc32(1, parseInt(statJSON[2].crc32_check, 10));
                setCrc32(2, parseInt(statJSON[3].crc32_check, 10));
                setCrc32(3, parseInt(statJSON[4].crc32_check, 10));

                addRxst(0, statJSON[1].rx_streams,
                           statJSON[1].rx_cir,
                           statJSON[1].rx_dir,
                           statJSON[1].rx_mir,
                           statJSON[1].rx_cdr,
                           statJSON[1].rx_cfr,
                           statJSON[1].rx_bitrate);
                addRxst(1, statJSON[2].rx_streams,
                           statJSON[2].rx_cir,
                           statJSON[2].rx_dir,
                           statJSON[2].rx_mir,
                           statJSON[2].rx_cdr,
                           statJSON[2].rx_cfr,
                           statJSON[2].rx_bitrate);
                addRxst(2, statJSON[3].rx_streams,
                           statJSON[3].rx_cir,
                           statJSON[3].rx_dir,
                           statJSON[3].rx_mir,
                           statJSON[3].rx_cdr,
                           statJSON[3].rx_cfr,
                           statJSON[3].rx_bitrate);
                addRxst(3, statJSON[4].rx_streams,
                           statJSON[4].rx_cir,
                           statJSON[4].rx_dir,
                           statJSON[4].rx_mir,
                           statJSON[4].rx_cdr,
                           statJSON[4].rx_cfr,
                           statJSON[4].rx_bitrate);

                addTxst(0, statJSON[1].tx_streams,
                           statJSON[1].tx_cir,
                           statJSON[1].tx_dir,
                           statJSON[1].tx_mir,
                           statJSON[1].tx_cdr,
                           statJSON[1].tx_cfr,
                           statJSON[1].tx_bitrate);
                addTxst(1, statJSON[2].tx_streams,
                           statJSON[2].tx_cir,
                           statJSON[2].tx_dir,
                           statJSON[2].tx_mir,
                           statJSON[2].tx_cdr,
                           statJSON[2].tx_cfr,
                           statJSON[2].tx_bitrate);
                addTxst(2, statJSON[3].tx_streams,
                           statJSON[3].tx_cir,
                           statJSON[3].tx_dir,
                           statJSON[3].tx_mir,
                           statJSON[3].tx_cdr,
                           statJSON[3].tx_cfr,
                           statJSON[3].tx_bitrate);
                addTxst(3, statJSON[4].tx_streams,
                           statJSON[4].tx_cir,
                           statJSON[4].tx_dir,
                           statJSON[4].tx_mir,
                           statJSON[4].tx_cdr,
                           statJSON[4].tx_cfr,
                           statJSON[4].tx_bitrate);

            })
            .fail(function() {
                console.log( "Error fail to get data from hub" );
            })
        }
    }, 1000);

    setInterval(function ()
    {
        if( !(gstatus == "HUBOFF" || gstatus == "MODOFF" || gstatus == "MLDROFF") )
        {
            $.ajax({
                type: "POST",
                url: mldrCheck(), //
                data: { request:$.toJSON({"command":"GET_RESPONSE"}), ip: lhs_ip() },
                timeout: 3000,
             })
            .done(function(data) {
                if( data !== "empty" )
                  log(msg, "Ответ " + data.toString());
            })
            .fail(function() {
                console.log( "Error fail to get response" );
            })
        }
    }, 1000);
});
