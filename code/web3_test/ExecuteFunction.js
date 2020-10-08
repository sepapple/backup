var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:7545'));

var abi = [
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "x",
          "type": "uint256"
        }
      ],
      "name": "set",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "get",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ];

address = "0x432Ff4D70AA6cc60353E6C9f5B203Fe66F968125";

const ExecuteFunction = ()=>{
    
    var myContract = new web3.eth.Contract(abi,address);

    myContract.methods.set(2).send({from: "0xEEeD5c2046310284e79FFBB6133648ac5af0C4d1"}).then(
    function(){ 
    myContract.methods.get().call().then(console.log);
    });
    //myContract.methods.get().call().then(console.log);
    
}

ExecuteFunction();
