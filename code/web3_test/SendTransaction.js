var Web3 = require('web3');
var web3 = new Web3();
web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));
web3.eth.personal.unlockAccount("0x70Ce5CcA21C79A5792059762CFAf366bC8D4020d", "test1", 10000)
.then(console.log('Account unlocked!'));
web3.eth.sendTransaction({
    from: '0x70Ce5CcA21C79A5792059762CFAf366bC8D4020d',
    to: '0x69ace8f4a119f06709a033df979c3b3da002f447',
    value: '100'
});


