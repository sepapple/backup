var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));

address = "0x4a235948b488efc12df71cc7ab083ac5f37512ed";

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
//sleep(100);

const GetTransactionBlock = ()=>{
    //ブロックの総数を取得
    web3.eth.getBlockNumber().then(function(data) {   
        var json = [];
         for (var i=5500; i<=data; i++){
           web3.eth.getBlock(i).then(function(transaction) {
               //配列が空か判定
               if(!isEmpty(transaction.transactions)){
                   //console.log(transaction.transactions);
                   var val = transaction.transactions;
                    //トランザクションからデータを取得
                   for(var i=0; i< val.length; i++){
                       web3.eth.getTransaction(val[i]).then(function(content){
                           //console.log(content);
                           if((content.input).length==202){ 
                               //対象範囲切り取り
                               var result_time = content.input.substr(63,11);
                               result_time = parseInt(result_time,16);
                               //console.log("time: "+result_time);
                               var result_lat = content.input.substr(130,8);
                               result_lat = parseInt(result_lat,16);
                               //console.log("lat: "+result_lat);
                               var result_lon = content.input.substr(193,9);
                               result_lon = parseInt(result_lon,16);
                               //console.log("lon: "+result_lon);
                               json.push({time: result_time,
                                          lat: result_lat,
                                          lon: result_lon});
                               console.log(json);
                           }
                       });
                   }    
               }
            }).catch(console.log);
        }
        console.log(json);
    }); 

   //web3.eth.getBlockTransactionCount("0x4a235948b488efc12df71cc7ab083ac5f37512ed").then(console.log);
}

GetTransactionBlock();
