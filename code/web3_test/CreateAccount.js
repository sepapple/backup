var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
var _account = web3.eth.personal.newAccount("test3").then(console.log);

