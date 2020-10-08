const Test = artifacts.require("CarContract");

module.exports = function(deployer) {
  deployer.deploy(Test);
};
