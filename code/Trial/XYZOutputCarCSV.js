var Web3 = require('web3');
const fs = require('fs');
const plotlib = require('nodeplotlib');

var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
const contract = JSON.parse(fs.readFileSync('/Users/sepa/truffle/Trial/build/contracts/CarContract.json','utf8'));
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
var datapath = "/Users/sepa/SensorData/XYZCarData";
datapath = datapath + process.argv[2] + ".csv";
const csvWriter = createCsvWriter({
    path: datapath,
    header: ['time','lat','lon','x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','y1','y2','y3','y4','y5','y6','y7','y8','y9','y10','z1','z2','z3','z4','z5','z6','z7','z8','z9','z10']
});
const abi = contract.abi;
const address = contract.networks[15].address;
var myID = 10;
var counter = 0;
var x_axis = [];
var y_axis = [];
var json = {};
var data = [];
var SMA = 0;
var temp_array = [];
var test = [];

function sleep(waitMsec){
    var startMsec = new Date();

    while (new Date() - startMsec < waitMsec);
}

function isEmpty(val){
    if(!val){

        if(val !== 0 && val !== false){
            return false;
        }

    }else if (typeof val == "object"){
        return Object.keys(val).length === 0;
    }

    return true;
}

function ExecuteFunction(){
        return new Promise(function (resolve,reject){
    var myContract = new web3.eth.Contract(abi,address);
    myContract.methods.CarGetData(myID,process.argv[2]).call().then(async function(ret){
        for(var i=ret.ret_array[6]; i<=ret.ret_array[7];i++){
            //配列が空か判定
            web3.eth.getBlock(i).then(function(transaction) {
                if(!isEmpty(transaction.transactions)){
                    //console.log(transaction.transactions);
                    var val = transaction.transactions;
                    //トランザクションからデータを取得
                    for(var i=0; i< val.length; i++){
                        web3.eth.getTransaction(val[i]).then(function(content){
                            if(content.input.length == 2570){
                                var result_id = content.input.substr(70,4);
                                result_id = parseInt(result_id,16);
                                //console.log("id: "+result_id);

                                if(result_id == 10){
                                    var result_time = content.input.substr(127,11);
                                    result_time = parseInt(result_time,16);

                                    var result_lat = content.input.substr(194,8);
                                    result_lat = parseInt(result_lat,16);
                                    //console.log("lat: "+result_lat);

                                    var result_lon = content.input.substr(258,8);
                                    result_lon = parseInt(result_lon,16);
                                    //console.log("lon: "+result_lon);

                                    var result_x1 = content.input.substr(578,8);
                                    const buffer_x1 = Buffer.from(result_x1, 'hex');
                                    result_x1 = buffer_x1.readInt32BE(0);
                                    //console.log("x1: "+result_x1);

                                    var result_x2 = content.input.substr(642,8);
                                    const buffer_x2 = Buffer.from(result_x2, 'hex');
                                    result_x2 = buffer_x2.readInt32BE(0);
                                    //console.log("x2: "+result_x2);

                                    var result_x3 = content.input.substr(706,8);
                                    const buffer_x3 = Buffer.from(result_x3, 'hex');
                                    result_x3 = buffer_x3.readInt32BE(0);
                                    //console.log("x3: "+result_x3);

                                    var result_x4 = content.input.substr(770,8);
                                    const buffer_x4 = Buffer.from(result_x4, 'hex');
                                    result_x4 = buffer_x4.readInt32BE(0);
                                    //console.log("x4: "+result_x4);

                                    var result_x5 = content.input.substr(834,8);
                                    const buffer_x5 = Buffer.from(result_x5, 'hex');
                                    result_x5 = buffer_x5.readInt32BE(0);
                                    //console.log("x5: "+result_x5);

                                    var result_x6 = content.input.substr(898,8);
                                    const buffer_x6 = Buffer.from(result_x6, 'hex');
                                    result_x6 = buffer_x6.readInt32BE(0);
                                    //console.log("x6: "+result_x6);

                                    var result_x7 = content.input.substr(962,8);
                                    const buffer_x7 = Buffer.from(result_x7, 'hex');
                                    result_x7 = buffer_x7.readInt32BE(0);
                                    //console.log("x7: "+result_x7);

                                    var result_x8 = content.input.substr(1026,8);
                                    const buffer_x8 = Buffer.from(result_x8, 'hex');
                                    result_x8 = buffer_x8.readInt32BE(0);
                                    //console.log("x8: "+result_x8);

                                    var result_x9 = content.input.substr(1090,8);
                                    const buffer_x9 = Buffer.from(result_x9, 'hex');
                                    result_x9 = buffer_x9.readInt32BE(0);
                                    //console.log("x9: "+result_x9);

                                    var result_x10 = content.input.substr(1154,8);
                                    const buffer_x10 = Buffer.from(result_x10, 'hex');
                                    result_x10 = buffer_x10.readInt32BE(0);
                                    //console.log("x10: "+result_x10);

                                    var result_y1 = content.input.substr(1282,8);
                                    const buffer_y1 = Buffer.from(result_y1, 'hex');
                                    result_y1 = buffer_y1.readInt32BE(0);
                                    //console.log("y1: "+result_y1);

                                    var result_y2 = content.input.substr(1346,8);
                                    const buffer_y2 = Buffer.from(result_y2, 'hex');
                                    result_y2 = buffer_y2.readInt32BE(0);
                                    //console.log("y2: "+result_y2);

                                    var result_y3 = content.input.substr(1410,8);
                                    const buffer_y3 = Buffer.from(result_y3, 'hex');
                                    result_y3 = buffer_y3.readInt32BE(0);
                                    //console.log("y3: "+result_y3);

                                    var result_y4 = content.input.substr(1474,8);
                                    const buffer_y4 = Buffer.from(result_y4, 'hex');
                                    result_y4 = buffer_y4.readInt32BE(0);
                                    //console.log("y4: "+result_y4);

                                    var result_y5 = content.input.substr(1538,8);
                                    const buffer_y5 = Buffer.from(result_y5, 'hex');
                                    result_y5 = buffer_y5.readInt32BE(0);
                                    //console.log("y5: "+result_y5);

                                    var result_y6 = content.input.substr(1602,8);
                                    const buffer_y6 = Buffer.from(result_y6, 'hex');
                                    result_y6 = buffer_y6.readInt32BE(0);
                                    //console.log("y6: "+result_y6);

                                    var result_y7 = content.input.substr(1666,8);
                                    const buffer_y7 = Buffer.from(result_y7, 'hex');
                                    result_y7 = buffer_y7.readInt32BE(0);
                                    //console.log("y7: "+result_y7);

                                    var result_y8 = content.input.substr(1730,8);
                                    const buffer_y8 = Buffer.from(result_y8, 'hex');
                                    result_y8 = buffer_y8.readInt32BE(0);
                                    //console.log("y8: "+result_y8);

                                    var result_y9 = content.input.substr(1794,8);
                                    const buffer_y9 = Buffer.from(result_y9, 'hex');
                                    result_y9 = buffer_y9.readInt32BE(0);
                                    //console.log("y9: "+result_y9);

                                    var result_y10 = content.input.substr(1858,8);
                                    const buffer_y10 = Buffer.from(result_y10, 'hex');
                                    result_y10 = buffer_y10.readInt32BE(0);
                                    //console.log("y10: "+result_y10);

                                    var result_z1 = content.input.substr(1986,8);
                                    const buffer_z1 = Buffer.from(result_z1, 'hex');
                                    result_z1 = buffer_z1.readInt32BE(0);
                                    // console.log("z1: "+result_z1);
                                    // x_axis.push(counter);
                                    


                                    var result_z2 = content.input.substr(2050,8);
                                    const buffer_z2 = Buffer.from(result_z2, 'hex');
                                    result_z2 = buffer_z2.readInt32BE(0);
                                    // console.log("z2: "+result_z2);
                                    // x_axis.push(counter);
                                    

                                    var result_z3 = content.input.substr(2114,8);
                                    const buffer_z3 = Buffer.from(result_z3, 'hex');
                                    result_z3 = buffer_z3.readInt32BE(0);
                                    // console.log("z3: "+result_z3);
                                    // x_axis.push(counter);
                                    

                                    var result_z4 = content.input.substr(2178,8);
                                    const buffer_z4 = Buffer.from(result_z4, 'hex');
                                    result_z4 = buffer_z4.readInt32BE(0);
                                    // console.log("z4: "+result_z4);
                                    // x_axis.push(counter);
                                    

                                    var result_z5 = content.input.substr(2242,8);
                                    const buffer_z5 = Buffer.from(result_z5, 'hex');
                                    result_z5 = buffer_z5.readInt32BE(0);
                                    // console.log("z5: "+result_z5);
                                    // x_axis.push(counter);
                                    

                                    var result_z6 = content.input.substr(2306,8);
                                    const buffer_z6 = Buffer.from(result_z6, 'hex');
                                    result_z6 = buffer_z6.readInt32BE(0);
                                    // console.log("z6: "+result_z6);
                                    // x_axis.push(counter);
                                    

                                    var result_z7 = content.input.substr(2370,8);
                                    const buffer_z7 = Buffer.from(result_z7, 'hex');
                                    result_z7 = buffer_z7.readInt32BE(0);
                                    //console.log("z7: "+result_z7);
                                    // x_axis.push(counter);
                                    

                                    var result_z8 = content.input.substr(2434,8);
                                    const buffer_z8 = Buffer.from(result_z8, 'hex');
                                    result_z8 = buffer_z8.readInt32BE(0);
                                    //console.log("z8: "+result_z8);
                                    // x_axis.push(counter);
                                    

                                    var result_z9 = content.input.substr(2498,8);
                                    const buffer_z9 = Buffer.from(result_z9, 'hex');
                                    result_z9 = buffer_z9.readInt32BE(0);
                                    //console.log("z9: "+result_z9);
                                    // x_axis.push(counter);
                                    

                                    var result_z10 = content.input.substr(2562,8);
                                    const buffer_z10 = Buffer.from(result_z10, 'hex');
                                    result_z10 = buffer_z10.readInt32BE(0);
                                    //console.log("z10: "+result_z10);
                                     // SMA = (result_z1/100000000+result_z2/100000000+result_z3/100000000+result_z4/100000000+result_z5/100000000+result_z6/100000000+result_z7/100000000+result_z8/100000000+result_z9/100000000+result_z10/100000000)/10;
                                    var temp = {};
                                    temp.time = result_time;
                                    temp.lat = result_lat/10000000;
                                    temp.lon = result_lon/10000000;
                                    temp.x1 = result_x1/100000000;
                                    temp.x2 = result_x2/100000000;
                                    temp.x3 = result_x3/100000000;
                                    temp.x4 = result_x4/100000000;
                                    temp.x5 = result_x5/100000000;
                                    temp.x6 = result_x6/100000000;
                                    temp.x7 = result_x7/100000000;
                                    temp.x8 = result_x8/100000000;
                                    temp.x9 = result_x9/100000000;
                                    temp.x10 = result_x10/100000000;
                                    temp.y1 = result_y1/100000000;
                                    temp.y2 = result_y2/100000000;
                                    temp.y3 = result_y3/100000000;
                                    temp.y4 = result_y4/100000000;
                                    temp.y5 = result_y5/100000000;
                                    temp.y6 = result_y6/100000000;
                                    temp.y7 = result_y7/100000000;
                                    temp.y8 = result_y8/100000000;
                                    temp.y9 = result_y9/100000000;
                                    temp.y10 = result_y10/100000000;
                                    temp.z1 = result_z1/100000000;
                                    temp.z2 = result_z2/100000000;
                                    temp.z3 = result_z3/100000000;
                                    temp.z4 = result_z4/100000000;
                                    temp.z5 = result_z5/100000000;
                                    temp.z6 = result_z6/100000000;
                                    temp.z7 = result_z7/100000000;
                                    temp.z8 = result_z8/100000000;
                                    temp.z9 = result_z9/100000000;
                                    temp.z10 = result_z10/100000000;

                                    // temp.z_axis = SMA;
                                    temp_array.push(temp);
                                     // console.log(temp_array);
                                    // console.log(temp_array);
                                     console.log(temp);
                                    //console.log(temp_array);
                                    //x_axis.push(result_time);
                                    // x_axis.push(counter);
                                    // y_axis.push(result_z10)/100000000;
                                    counter++;
                                }
                            }
                        })
                    }

                }
            });
        }

    });
});
}

function showdata(){
    //ソート
    temp_array.sort(function(a,b){
        if(a.time<b.time) return -1;
        if(a.time > b.time) return 1;
        return 0;
    });

    console.log(temp_array);
    console.log("データ数: "+counter);

    //csvファイルに書き出し
    csvWriter.writeRecords(temp_array).then(console.log('done'));
}


ExecuteFunction();

setTimeout(showdata,3000);
