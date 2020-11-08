package com.example.trial_swarm;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.Callable;
import org.web3j.abi.TypeReference;
import org.web3j.abi.datatypes.Function;
import org.web3j.abi.datatypes.Type;
import org.web3j.abi.datatypes.generated.StaticArray8;
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
    public static final String BINARY = "608060405234801561001057600080fd5b506107b6806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c806329d3f0fb146100515780637d50a9ec14610076578063d8ebbb09146100a5578063e6f961de146101de575b600080fd5b6100746004803603604081101561006757600080fd5b508035906020013561023a565b005b6100746004803603608081101561008c57600080fd5b508035906020810135906040810135906060013561037a565b610074600480360360808110156100bb57600080fd5b8135916020810135918101906060810160408201356401000000008111156100e257600080fd5b8201836020820111156100f457600080fd5b8035906020019184600183028401116401000000008311171561011657600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600092019190915250929594936020810193503591505064010000000081111561016957600080fd5b82018360208201111561017b57600080fd5b8035906020019184600183028401116401000000008311171561019d57600080fd5b91908080601f0160208091040260200160405190810160405280939291908181526020018383808284376000920191909152509295506103b9945050505050565b610201600480360360408110156101f457600080fd5b508035906020013561043b565b604051808261010080838360005b8381101561022757818101518382015260200161020f565b5050505090500191505060405180910390f35b6000828152600160205260409020600301546001600160a01b0316331461026057600080fd5b60008281526001602081815260408084206008810186905543600a82015584835290842083835280548085018255908552919093208354600b9092020190815582820154818301556002808401548183015560038085015490830180546001600160a01b0319166001600160a01b0390921691909117905560048085015490830155600580850180549394610308949286019391929081161561010002600019011604610651565b5060068201816006019080546001816001161561010002031660029004610330929190610651565b50600782810154908201556008808301549082015560098083015490820155600a9182015491015550600090815260016020526040902060030180546001600160a01b0319169055565b60008481526001602081905260409091209485558401929092556007830155600282015543600982015560030180546001600160a01b03191633179055565b6000848152600160205260409020600301546001600160a01b031633146103df57600080fd5b600084815260016020908152604090912085815560048101859055835161040e926005909201918501906106d6565b5060008481526001602090815260409091208251610434926006909201918401906106d6565b5050505050565b610443610744565b600083815260208190526040902080548390811061045d57fe5b60009182526020808320600b929092029091015483528482528190526040902080548390811061048957fe5b90600052602060002090600b020160040154816001600881106104a857fe5b60200201818152505060008084815260200190815260200160002082815481106104ce57fe5b90600052602060002090600b020160070154816002600881106104ed57fe5b602002018181525050600080848152602001908152602001600020828154811061051357fe5b90600052602060002090600b0201600801548160036008811061053257fe5b602002018181525050600080848152602001908152602001600020828154811061055857fe5b90600052602060002090600b0201600901548160046008811061057757fe5b602002018181525050600080848152602001908152602001600020828154811061059d57fe5b90600052602060002090600b0201600a0154816005600881106105bc57fe5b60200201818152505060008084815260200190815260200160002082815481106105e257fe5b90600052602060002090600b0201600101548160066008811061060157fe5b602002018181525050600080848152602001908152602001600020828154811061062757fe5b90600052602060002090600b0201600201548160076008811061064657fe5b602002015292915050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061068a57805485556106c6565b828001600101855582156106c657600052602060002091601f016020900482015b828111156106c65782548255916001019190600101906106ab565b506106d2929150610763565b5090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061071757805160ff19168380011785556106c6565b828001600101855582156106c6579182015b828111156106c6578251825591602001919060010190610729565b6040518061010001604052806008906020820280368337509192915050565b61077d91905b808211156106d25760008155600101610769565b9056fea2646970667358221220b53fc6bd883c67e7edf2ff218ebe121ea9953f780ccb9d034cab47df1bc5e4a664736f6c63430006080033";

    public static final String FUNC_USERFINISH = "UserFinish";

    public static final String FUNC_USERGETDATA = "UserGetData";

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

    public RemoteFunctionCall<TransactionReceipt> UserFinish(BigInteger _myID, BigInteger _time) {
        final Function function = new Function(
                FUNC_USERFINISH, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_time)), 
                Collections.<TypeReference<?>>emptyList());
        return executeRemoteCallTransaction(function);
    }

    public RemoteFunctionCall<List> UserGetData(BigInteger _myID, BigInteger _num) {
        final Function function = new Function(FUNC_USERGETDATA, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_num)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<StaticArray8<Uint256>>() {}));
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

    public RemoteFunctionCall<TransactionReceipt> UserStart(BigInteger _myID, BigInteger _PartnerID, BigInteger _time, BigInteger _ConnectionID) {
        final Function function = new Function(
                FUNC_USERSTART, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_PartnerID), 
                new org.web3j.abi.datatypes.generated.Uint256(_time), 
                new org.web3j.abi.datatypes.generated.Uint256(_ConnectionID)), 
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
