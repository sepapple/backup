var keythereum = require("keythereum-pure-js");
var keyobj=keythereum.importFromFile('0xefc4835180bdb5079484ab6f7f87650c15749f07','/Users/sepa/Trial/');
var privateKey=keythereum.recover('password',keyobj);

console.log(privateKey.toString('hex'));


