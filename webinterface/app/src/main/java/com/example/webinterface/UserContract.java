package com.example.webinterface;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.Callable;
import org.web3j.abi.TypeReference;
import org.web3j.abi.datatypes.Function;
import org.web3j.abi.datatypes.Type;
import org.web3j.abi.datatypes.generated.StaticArray12;
import org.web3j.abi.datatypes.generated.Uint256;
import org.web3j.crypto.Credentials;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.RemoteCall;
import org.web3j.protocol.core.RemoteFunctionCall;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.tx.Contract;
import org.web3j.tx.TransactionManager;
import org.web3j.tx.gas.ContractGasProvider;

/**
 * <p>Auto generated code.
 * <p><strong>Do not modify!</strong>
 * <p>Please use the <a href="https://docs.web3j.io/command_line.html">web3j command line tools</a>,
 * or the org.web3j.codegen.SolidityFunctionWrapperGenerator in the 
 * <a href="https://github.com/web3j/web3j/tree/master/codegen">codegen module</a> to update.
 *
 * <p>Generated with web3j version 4.5.16.
 */
@SuppressWarnings("rawtypes")
public class UserContract extends Contract {
    public static final String BINARY = "608060405234801561001057600080fd5b50610994806100206000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c80632b817a2e1461005c578063d741e1611461008b578063d8ebbb09146100c8578063e6f961de14610201578063fbb7a0b11461025d575b600080fd5b6100796004803603602081101561007257600080fd5b503561028c565b60408051918252519081900360200190f35b6100c6600480360360c08110156100a157600080fd5b5080359060208101359060408101359060608101359060808101359060a0013561029e565b005b6100c6600480360360808110156100de57600080fd5b81359160208101359181019060608101604082013564010000000081111561010557600080fd5b82018360208201111561011757600080fd5b8035906020019184600183028401116401000000008311171561013957600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929594936020810193503591505064010000000081111561018c57600080fd5b82018360208201111561019e57600080fd5b803590602001918460018302840111640100000000831117156101c057600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295506102ee945050505050565b6102246004803603604081101561021757600080fd5b5080359060200135610370565b604051808261018080838360005b8381101561024a578181015183820152602001610232565b5050505090500191505060405180910390f35b6100c66004803603608081101561027357600080fd5b50803590602081013590604081013590606001356106a5565b60009081526020819052604090205490565b60008681526002602081905260409091209687556001870195909555600786019390935592840155600b830191909155600c82015543600982015560030180546001600160a01b03191633179055565b6000848152600260205260409020600301546001600160a01b0316331461031457600080fd5b60008481526002602090815260409091208581556004810185905583516103439260059092019185019061082f565b50600084815260026020908152604090912082516103699260069092019184019061082f565b5050505050565b6103786108ad565b600083815260016020526040902080548390811061039257fe5b60009182526020808320600f9290920290910154835284825260019052604090208054839081106103bf57fe5b90600052602060002090600f020160040154816001600c81106103de57fe5b60200201818152505060016000848152602001908152602001600020828154811061040557fe5b90600052602060002090600f020160070154816002600c811061042457fe5b60200201818152505060016000848152602001908152602001600020828154811061044b57fe5b90600052602060002090600f020160080154816003600c811061046a57fe5b60200201818152505060016000848152602001908152602001600020828154811061049157fe5b90600052602060002090600f020160090154816004600c81106104b057fe5b6020020181815250506001600084815260200190815260200160002082815481106104d757fe5b90600052602060002090600f0201600a0154816005600c81106104f657fe5b60200201818152505060016000848152602001908152602001600020828154811061051d57fe5b90600052602060002090600f020160010154816006600c811061053c57fe5b60200201818152505060016000848152602001908152602001600020828154811061056357fe5b90600052602060002090600f020160020154816007600c811061058257fe5b6020020181815250506001600084815260200190815260200160002082815481106105a957fe5b90600052602060002090600f0201600b0154816008600c81106105c857fe5b6020020181815250506001600084815260200190815260200160002082815481106105ef57fe5b90600052602060002090600f0201600c0154816009600c811061060e57fe5b60200201818152505060016000848152602001908152602001600020828154811061063557fe5b90600052602060002090600f0201600d015481600a600c811061065457fe5b60200201818152505060016000848152602001908152602001600020828154811061067b57fe5b90600052602060002090600f0201600e015481600b600c811061069a57fe5b602002015292915050565b6000848152600260205260409020600301546001600160a01b031633146106cb57600080fd5b60008481526002602081815260408084206008810188905543600a820155600d8101879055600e8101869055600180845291852084845280548084018255908652929094208454600f909302019182558084015482820155838301548284015560038085015490830180546001600160a01b0319166001600160a01b039092169190911790556004808501549083015560058085018054939461078394928601939192918216156101000260001901909116046108cc565b50600682018160060190805460018160011615610100020316600290046107ab9291906108cc565b50600782810154908201556008808301549082015560098083015490820155600a8083015490820155600b8083015490820155600c8083015490820155600d8083015490820155600e91820154910155505050600090815260026020908152604080832060030180546001600160a01b031916905590829052902080546001019055565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061087057805160ff191683800117855561089d565b8280016001018555821561089d579182015b8281111561089d578251825591602001919060010190610882565b506108a9929150610941565b5090565b604051806101800160405280600c906020820280368337509192915050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10610905578054855561089d565b8280016001018555821561089d57600052602060002091601f016020900482015b8281111561089d578254825591600101919060010190610926565b61095b91905b808211156108a95760008155600101610947565b9056fea2646970667358221220ec18689067bea497b5e717b894c4b6e628a91ae823c7a513a8e2fe74efd1a4bc64736f6c63430006080033";

    public static final String FUNC_USERFINISH = "UserFinish";

    public static final String FUNC_USERGETDATA = "UserGetData";

    public static final String FUNC_USERGETRIDENUM = "UserGetRideNum";

    public static final String FUNC_USERREGISTDATA = "UserRegistData";

    public static final String FUNC_USERSTART = "UserStart";

    @Deprecated
    protected UserContract(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    protected UserContract(String contractAddress, Web3j web3j, Credentials credentials, ContractGasProvider contractGasProvider) {
        super(BINARY, contractAddress, web3j, credentials, contractGasProvider);
    }

    @Deprecated
    protected UserContract(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        super(BINARY, contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    protected UserContract(String contractAddress, Web3j web3j, TransactionManager transactionManager, ContractGasProvider contractGasProvider) {
        super(BINARY, contractAddress, web3j, transactionManager, contractGasProvider);
    }

    public RemoteFunctionCall<TransactionReceipt> UserFinish(BigInteger _myID, BigInteger _time, BigInteger _lat, BigInteger _lon) {
        final Function function = new Function(
                FUNC_USERFINISH, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_time), 
                new org.web3j.abi.datatypes.generated.Uint256(_lat), 
                new org.web3j.abi.datatypes.generated.Uint256(_lon)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteFunctionCall<List> UserGetData(BigInteger _myID, BigInteger _num) {
        final Function function = new Function(FUNC_USERGETDATA, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_num)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<StaticArray12<Uint256>>() {}));
        return new RemoteFunctionCall<List>(function,
                new Callable<List>() {
                    @Override
                    @SuppressWarnings("unchecked")
                    public List call() throws Exception {
                        List<Type> result = (List<Type>) executeCallSingleValueReturn(function, List.class);
                        return convertToNative(result);
                    }
                });
    }

    public RemoteFunctionCall<BigInteger> UserGetRideNum(BigInteger _myID) {
        final Function function = new Function(FUNC_USERGETRIDENUM, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<Uint256>() {}));
        return executeRemoteCallSingleValueReturn(function, BigInteger.class);
    }

    public RemoteFunctionCall<TransactionReceipt> UserRegistData(BigInteger _myID, BigInteger _time, String _high, String _low) {
        final Function function = new Function(
                FUNC_USERREGISTDATA, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_time), 
                new org.web3j.abi.datatypes.Utf8String(_high), 
                new org.web3j.abi.datatypes.Utf8String(_low)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteFunctionCall<TransactionReceipt> UserStart(BigInteger _myID, BigInteger _PartnerID, BigInteger _time, BigInteger _ConnectionID, BigInteger _lat, BigInteger _lon) {
        final Function function = new Function(
                FUNC_USERSTART, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_PartnerID), 
                new org.web3j.abi.datatypes.generated.Uint256(_time), 
                new org.web3j.abi.datatypes.generated.Uint256(_ConnectionID), 
                new org.web3j.abi.datatypes.generated.Uint256(_lat), 
                new org.web3j.abi.datatypes.generated.Uint256(_lon)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    @Deprecated
    public static UserContract load(String contractAddress, Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return new UserContract(contractAddress, web3j, credentials, gasPrice, gasLimit);
    }

    @Deprecated
    public static UserContract load(String contractAddress, Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return new UserContract(contractAddress, web3j, transactionManager, gasPrice, gasLimit);
    }

    public static UserContract load(String contractAddress, Web3j web3j, Credentials credentials, ContractGasProvider contractGasProvider) {
        return new UserContract(contractAddress, web3j, credentials, contractGasProvider);
    }

    public static UserContract load(String contractAddress, Web3j web3j, TransactionManager transactionManager, ContractGasProvider contractGasProvider) {
        return new UserContract(contractAddress, web3j, transactionManager, contractGasProvider);
    }

    public static RemoteCall<UserContract> deploy(Web3j web3j, Credentials credentials, ContractGasProvider contractGasProvider) {
        return deployRemoteCall(UserContract.class, web3j, credentials, contractGasProvider, BINARY, "");
    }

    @Deprecated
    public static RemoteCall<UserContract> deploy(Web3j web3j, Credentials credentials, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(UserContract.class, web3j, credentials, gasPrice, gasLimit, BINARY, "");
    }

    public static RemoteCall<UserContract> deploy(Web3j web3j, TransactionManager transactionManager, ContractGasProvider contractGasProvider) {
        return deployRemoteCall(UserContract.class, web3j, transactionManager, contractGasProvider, BINARY, "");
    }

    @Deprecated
    public static RemoteCall<UserContract> deploy(Web3j web3j, TransactionManager transactionManager, BigInteger gasPrice, BigInteger gasLimit) {
        return deployRemoteCall(UserContract.class, web3j, transactionManager, gasPrice, gasLimit, BINARY, "");
    }
}
