var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:7545'));
var abi = [
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "Datas",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "time",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "lat",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "lon",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "OwnerToDataCount",
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
    },
    {
      "constant": false,
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_time",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_lat",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_lon",
          "type": "uint256"
        }
      ],
      "name": "DataSet",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "getDataByOwner",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "_time",
          "type": "uint256[]"
        },
        {
          "internalType": "uint256[]",
          "name": "_lat",
          "type": "uint256[]"
        },
        {
          "internalType": "uint256[]",
          "name": "_lon",
          "type": "uint256[]"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ];

address = "0x30a97f7290EAA7903862957e554b713A129456bA";

const ExecuteFunction = ()=>{
    
    var myContract = new web3.eth.Contract(abi,address);

    var lat = 3476673167;
    var lon = 13547904167;
    var data_obj = new Date();
    var time = data_obj.getTime();
    myContract.methods.DataSet(time,lat,lon).send({from:"0x95a2dc6F449E1dc04b43aB9408185CbB5058D449",gas:3000000}).then(console.log);
    //myContract.methods.GetData(0).call().then(console.log)
}
    //function(){ 
    //myContract.methods.get().call().then(console.log);}


ExecuteFunction();
