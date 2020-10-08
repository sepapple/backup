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
    myContract.methods.UserGetData(myID,60).call().then(function(ret){
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
                                console.log(content.input)
                               var result_time = content.input.substr(63,11);
                            }
                        })
                    }
                }
            });
        }
    });




        // web3.eth.getBlock(7539).then(function(transaction) {
        //     var val = transaction.transactions;
        //     for(var i=0; i< val.length; i++){
        //         web3.eth.getTransaction(val[i]).then(console.log);
        //     }
        // });
    
    //myContract.methods.get().call().then(console.log);

    //function(){ 
        //myContract.methods.get().call().then(console.log);
        //myContract.methods.set(2).send({from: "0xEEeD5c2046310284e79FFBB6133648ac5af0C4d1"}).then(
}

ExecuteFunction();
