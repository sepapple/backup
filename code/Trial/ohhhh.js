var Web3 = require('web3');
const fs = require('fs');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
const contract = JSON.parse(fs.readFileSync('/Users/sepa/truffle/Trial/build/contracts/UserContract.json','utf8'));
const abi = contract.abi;
const address = contract.networks[15].address;
var myID = 100;

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

const ExecuteFunction = ()=>{
    var myContract = new web3.eth.Contract(abi,address);
    myContract.methods.UserGetData(myID,37).call().then(function(ret){
        for(var i=ret.ret_array[6]; i<=ret.ret_array[7];i++){
            //配列が空か判定
            web3.eth.getBlock(i).then(function(transaction) {
                if(!isEmpty(transaction.transactions)){
                    console.log(transaction.transactions);
                    var val = transaction.transactions;
                    //トランザクションからデータを取得
                    for(var i=0; i< val.length; i++){
                        web3.eth.getTransaction(val[i]).then(function(content){
                            if(content.input.length == 2570){
                                //console.log(content.input);
                                // var result_id = content.input.substr(70,4);
                                // result_id = parseInt(result_id,16);
                                // console.log("id: "+result_id);
                                // 
                                // var result_time = content.input.substr(127,11);
                                // result_time = parseInt(result_time,16);
                                // console.log("time: "+result_time);
                                // 
                                // var result_lat = content.input.substr(194,8);
                                // result_lat = parseInt(result_lat,16);
                                // console.log("lat: "+result_lat);
                                // 
                                // var result_lon = content.input.substr(258,8);
                                // result_lon = parseInt(result_lon,16);
                                // console.log("lon: "+result_lon);
                                // 
                                // var result_x1 = content.input.substr(578,8);
                                // const buffer_x1 = Buffer.from(result_x1, 'hex');
                                // result_x1 = buffer_x1.readIntBE(0);
                                // console.log("x1: "+result_x1);
                                // 
                                // var result_x2 = content.input.substr(642,8);
                                // const buffer_x2 = Buffer.from(result_x2, 'hex');
                                // result_x2 = buffer_x2.readInt32BE(0);
                                // console.log("x2: "+result_x2);
                                // 
                                // var result_x3 = content.input.substr(706,8);
                                // const buffer_x3 = Buffer.from(result_x3, 'hex');
                                // result_x3 = buffer_x3.readInt32BE(0);
                                // console.log("x3: "+result_x3);
                                // 
                                // var result_x4 = content.input.substr(770,8);
                                // const buffer_x4 = Buffer.from(result_x4, 'hex');
                                // result_x4 = buffer_x4.readInt32BE(0);
                                // console.log("x4: "+result_x4);
                                // 
                                // var result_x5 = content.input.substr(834,8);
                                // const buffer_x5 = Buffer.from(result_x5, 'hex');
                                // result_x5 = buffer_x5.readInt32BE(0);
                                // console.log("x5: "+result_x5);
                                // 
                                // var result_x6 = content.input.substr(898,8);
                                // const buffer_x6 = Buffer.from(result_x6, 'hex');
                                // result_x6 = buffer_x6.readInt32BE(0);
                                // console.log("x6: "+result_x6);
                                // 
                                // var result_x7 = content.input.substr(962,8);
                                // const buffer_x7 = Buffer.from(result_x7, 'hex');
                                // result_x7 = buffer_x7.readInt32BE(0);
                                // console.log("x7: "+result_x7);
                                // 
                                // var result_x8 = content.input.substr(1026,8);
                                // const buffer_x8 = Buffer.from(result_x8, 'hex');
                                // result_x8 = buffer_x8.readInt32BE(0);
                                // console.log("x8: "+result_x8);
                                // 
                                // var result_x9 = content.input.substr(1090,8);
                                // const buffer_x9 = Buffer.from(result_x9, 'hex');
                                // result_x9 = buffer_x9.readInt32BE(0);
                                // console.log("x9: "+result_x9);
                                // 
                                // var result_x10 = content.input.substr(1154,8);
                                // const buffer_x10 = Buffer.from(result_x10, 'hex');
                                // result_x10 = buffer_x10.readInt32BE(0);
                                // console.log("x10: "+result_x10);
                                // 
                                // var result_y1 = content.input.substr(1283,8);
                                // const buffer_y1 = Buffer.from(result_y1, 'hex');
                                // result_y1 = buffer_y1.readInt32BE(0);
                                // console.log("y1: "+result_y1);
                                // 
                                // var result_y2 = content.input.substr(1347,8);
                                // const buffer_y2 = Buffer.from(result_y2, 'hex');
                                // result_y2 = buffer_y2.readInt32BE(0);
                                // console.log("y2: "+result_y2);
                                // 
                                // var result_y3 = content.input.substr(1411,8);
                                // const buffer_y3 = Buffer.from(result_y3, 'hex');
                                // result_y3 = buffer_y3.readInt32BE(0);
                                // console.log("y3: "+result_y3);
                                // 
                                // var result_y4 = content.input.substr(1475,8);
                                // const buffer_y4 = Buffer.from(result_y4, 'hex');
                                // result_y4 = buffer_y4.readInt32BE(0);
                                // console.log("y4: "+result_y4);
                                // 
                                // var result_y5 = content.input.substr(1539,8);
                                // const buffer_y5 = Buffer.from(result_y5, 'hex');
                                // result_y5 = buffer_y5.readInt32BE(0);
                                // console.log("y5: "+result_y5);
                                // 
                                // var result_y6 = content.input.substr(1603,8);
                                // const buffer_y6 = Buffer.from(result_y6, 'hex');
                                // result_y6 = buffer_y6.readInt32BE(0);
                                // console.log("y6: "+result_y6);
                                // 
                                // var result_y7 = content.input.substr(1667,8);
                                // const buffer_y7 = Buffer.from(result_y7, 'hex');
                                // result_y7 = buffer_y7.readInt32BE(0);
                                // console.log("y7: "+result_y7);
                                // 
                                // var result_y8 = content.input.substr(1731,8);
                                // const buffer_y8 = Buffer.from(result_y8, 'hex');
                                // result_y8 = buffer_y8.readInt32BE(0);
                                // console.log("y8: "+result_y8);
                                // 
                                // var result_y9 = content.input.substr(1795,8);
                                // const buffer_y9 = Buffer.from(result_y9, 'hex');
                                // result_y9 = buffer_y9.readInt32BE(0);
                                // console.log("y9: "+result_y9);
                                // 
                                // var result_y10 = content.input.substr(1859,8);
                                // const buffer_y10 = Buffer.from(result_y10, 'hex');
                                // result_y10 = buffer_y10.readInt32BE(0);
                                // console.log("y10: "+result_y10);
                            }
                        })
                    }
                }
            });
        }
    });
}

ExecuteFunction();

