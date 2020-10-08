var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://192.168.30.30:7545'));
web3.eth.getBalance("0x2DE9906BAe4d654fb46E22CC6117755eDE845C55").then(console.log);

//web3.eth.getBalance("0x6d4a7410de1f03775828b05a266aaa5d9aa1c29e").then(console.log);
