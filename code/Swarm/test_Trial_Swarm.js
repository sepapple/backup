var Web3 = require('web3');
const fs = require('fs');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
const contract = JSON.parse(fs.readFileSync('/Users/sepa/ethereum/SmartContract/Trial_Swarm/build/contracts/CarContract.json','utf8'));
const abi = contract.abi;
const address = contract.networks[15].address;

var str = "a8229c93f7941b090e5826154f54a329dc43bf22f66de513f0cfad075f00c8ac"
// var high = str.substr(0,32);
// var low = str.substr(32,32);
const ExecuteFunction = ()=>{
    var myContract = new web3.eth.Contract(abi,address);
    web3.eth.getAccounts().then(function(data){
            myContract.methods.CarGetData(10,process.argv[2]).call().then(console.log)
        });

}

ExecuteFunction();

