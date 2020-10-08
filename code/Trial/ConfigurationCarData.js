var Web3 = require('web3');
const fs = require('fs');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
const contract = JSON.parse(fs.readFileSync('/Users/sepa/truffle/Trial/build/contracts/CarContract.json','utf8'));
const abi = contract.abi;
const address = contract.networks[15].address;
var myID = 10;
const ExecuteFunction = ()=>{
    var myContract = new web3.eth.Contract(abi,address);
    myContract.methods.CarGetData(myID,process.argv[2]).call().then(function(value){
        console.log(process.argv[2]+"'sConnectionID: "+value.ret_array[9]);
        console.log(value);
    });
    //myContract.methods.get().call().then(console.log);
    
    //function(){ 
    //myContract.methods.get().call().then(console.log);
    //myContract.methods.set(2).send({from: "0xEEeD5c2046310284e79FFBB6133648ac5af0C4d1"}).then(
}

ExecuteFunction();

