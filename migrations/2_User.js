const Test = artifacts.require("UserContract");

module.exports = function(deployer) {
  deployer.deploy(Test);
};
