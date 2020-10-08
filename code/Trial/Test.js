var Web3 = require('web3');
const fs = require('fs');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:7545'));
const contract = JSON.parse(fs.readFileSync('/Users/sepa/truffle/Trial/build/contracts/Test.json','utf8'));
const abi = contract.abi;
const address = contract.networks[5777].address;
const ExecuteFunction = ()=>{
    var myContract = new web3.eth.Contract(abi,address);
    web3.eth.getAccounts().then(function(data){
        myContract.methods.UserStart().send({from: data[0],gas: 300000}).then(
            myContract.methods.UserRegistData(100).send({from: data[0],gas: 3000000}).then(console.log)
        )
    });
}

ExecuteFunction();
