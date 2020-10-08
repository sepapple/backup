var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
abi = [
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
address = "0xf89760B9117AfCb4349a7D58EE02358dAB11979a";
const GPS_get = ()=>{
    var myContract = new web3.eth.Contract(abi,address);
    myContract.methods.getDataByOwner().call().then(console.log)


}

GPS_get();
