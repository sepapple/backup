const fs = require('fs');
//const jsonObject = require('/users/sepa/truffle/trial/build/contracts/usercontract.json');
let jsonObject = JSON.parse( fs.readFileSync('/Users/sepa/truffle/Trial/build/contracts/UserContract.json','utf8'));
//let jsonObject = fs.readFileSync('/users/sepa/truffle/trial/build/contracts/usercontract.json','utf8');
console.log(JSON.stringify(jsonObject.abi));
//console.log(jsonobject.networks.5777.address);
console.log(jsonObject.networks[5777].address);
