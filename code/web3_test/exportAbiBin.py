import json

path = "/Users/sepa/truffle/GPS/build/contracts/GPSRegister.json"

truffleFile = json.load(open(path))

print(truffleFile['abi'])
print(truffleFile['bytecode'])
