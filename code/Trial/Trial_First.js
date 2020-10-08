var Web3 = require('web3');
const fs = require('fs');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:7545'));
const contract = JSON.parse(fs.readFileSync('/Users/sepa/truffle/Trial/build/contracts/UserContract.json','utf8'));
const abi = contract.abi;
var accel = [0,0,0,0,0,0,0,0,0,0]; 
var myID = 10;
var PartnerID = 20;
const address = contract.networks[5777].address;
const ExecuteFunction = ()=>{
    var myContract = new web3.eth.Contract(abi,address);
    web3.eth.getAccounts().then(function(data){
        myContract.methods.UserStart(myID,PartnerID,5454,2434).send({from: data[0],gas: 300000}).then(
            myContract.methods.UserRegistData(myID,3939,1000,10000,accel,accel,accel).send({from: data[0],gas: 3000000}).then(
                myContract.methods.UserFinish(myID,114514).send({from: data[0],gas: 3000000}).then(
                    myContract.methods.UserGetData(myID,1).call().then(console.log)   
                )
            )
        )
    });
    //myContract.methods.get().call().then(console.log);
    
    //function(){ 
    //myContract.methods.get().call().then(console.log);
    //myContract.methods.set(2).send({from: "0xEEeD5c2046310284e79FFBB6133648ac5af0C4d1"}).then(
}

ExecuteFunction();
