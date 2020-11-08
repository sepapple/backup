package com.example.trial;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.Callable;
import org.web3j.abi.TypeReference;
import org.web3j.abi.datatypes.DynamicArray;
import org.web3j.abi.datatypes.Function;
import org.web3j.abi.datatypes.Type;
import org.web3j.abi.datatypes.generated.Int256;
import org.web3j.abi.datatypes.generated.StaticArray10;
import org.web3j.abi.datatypes.generated.Uint256;
import org.web3j.crypto.Credentials;
import org.web3j.protocol.Web3j;
import org.web3j.protocol.core.RemoteCall;
import org.web3j.protocol.core.RemoteFunctionCall;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.tuples.generated.Tuple4;
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
    public static final String BINARY = "608060405234801561001057600080fd5b50610adc806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c806329d3f0fb146100515780632a73fab4146100765780637d50a9ec14610239578063e6f961de14610268575b600080fd5b6100746004803603604081101561006757600080fd5b5080359060200135610393565b005b610074600480360360e081101561008c57600080fd5b81359160208101359160408201359160608101359181019060a0810160808201356401000000008111156100bf57600080fd5b8201836020820111156100d157600080fd5b803590602001918460208302840111640100000000831117156100f357600080fd5b919080806020026020016040519081016040528093929190818152602001838360200280828437600092019190915250929594936020810193503591505064010000000081111561014357600080fd5b82018360208201111561015557600080fd5b8035906020019184602083028401116401000000008311171561017757600080fd5b91908080602002602001604051908101604052809392919081815260200183836020028082843760009201919091525092959493602081019350359150506401000000008111156101c757600080fd5b8201836020820111156101d957600080fd5b803590602001918460208302840111640100000000831117156101fb57600080fd5b9190808060200260200160405190810160405280939291908181526020018383602002808284376000920191909152509295506104bf945050505050565b6100746004803603608081101561024f57600080fd5b5080359060208101359060408101359060600135610578565b61028b6004803603604081101561027e57600080fd5b50803590602001356105b7565b604051808561014080838360005b838110156102b1578181015183820152602001610299565b50505050905001806020018060200180602001848103845287818151815260200191508051906020019060200280838360005b838110156102fc5781810151838201526020016102e4565b50505050905001848103835286818151815260200191508051906020019060200280838360005b8381101561033b578181015183820152602001610323565b50505050905001848103825285818151815260200191508051906020019060200280838360005b8381101561037a578181015183820152602001610362565b5050505090500197505050505050505060405180910390f35b6000828152600160205260409020600301546001600160a01b031633146103b957600080fd5b6000828152600160208181526040808420600b810186905543600d82015584835290842083835280548085018255908552919093208354600e9092020190815582820154918101919091556002808301549082015560038083015490820180546001600160a01b0319166001600160a01b039092169190911790556004808301549082015560058083015490820155600680830154908201556007808301805461046692840191906109df565b506008828101805461047b92840191906109df565b506009828101805461049092840191906109df565b50600a82015481600a0155600b82015481600b0155600c82015481600c0155600d82015481600d015550505050565b6000878152600160205260409020600301546001600160a01b031633146104e557600080fd5b6000878152600160209081526040909120888155600481018890556005810187905560068101869055845161052292600790920191860190610a2f565b506000878152600160209081526040909120835161054892600890920191850190610a2f565b506000878152600160209081526040909120825161056e92600990920191840190610a2f565b5050505050505050565b6000848152600160208190526040909120948555840192909255600a830155600282015543600c82015560030180546001600160a01b03191633179055565b6105bf610a6a565b606080606060008087815260200190815260200160002085815481106105e157fe5b60009182526020808320600e929092029091015486528782528190526040902080548690811061060d57fe5b90600052602060002090600e020160040154846001600a811061062c57fe5b602002018181525050600080878152602001908152602001600020858154811061065257fe5b90600052602060002090600e020160050154846002600a811061067157fe5b602002018181525050600080878152602001908152602001600020858154811061069757fe5b90600052602060002090600e020160060154846003600a81106106b657fe5b60200201818152505060008087815260200190815260200160002085815481106106dc57fe5b90600052602060002090600e020160070180548060200260200160405190810160405280929190818152602001828054801561073757602002820191906000526020600020905b815481526020019060010190808311610723575b50505050509250600080878152602001908152602001600020858154811061075b57fe5b90600052602060002090600e02016008018054806020026020016040519081016040528092919081815260200182805480156107b657602002820191906000526020600020905b8154815260200190600101908083116107a2575b5050505050915060008087815260200190815260200160002085815481106107da57fe5b90600052602060002090600e020160090180548060200260200160405190810160405280929190818152602001828054801561083557602002820191906000526020600020905b815481526020019060010190808311610821575b50505050509050600080878152602001908152602001600020858154811061085957fe5b90600052602060002090600e0201600a0154846004600a811061087857fe5b602002018181525050600080878152602001908152602001600020858154811061089e57fe5b90600052602060002090600e0201600b0154846005600a81106108bd57fe5b60200201818152505060008087815260200190815260200160002085815481106108e357fe5b90600052602060002090600e0201600c0154846006600a811061090257fe5b602002018181525050600080878152602001908152602001600020858154811061092857fe5b90600052602060002090600e0201600d0154846007600a811061094757fe5b602002018181525050600080878152602001908152602001600020858154811061096d57fe5b90600052602060002090600e020160010154846008600a811061098c57fe5b60200201818152505060008087815260200190815260200160002085815481106109b257fe5b90600052602060002090600e020160020154846009600a81106109d157fe5b602002015292959194509250565b828054828255906000526020600020908101928215610a1f5760005260206000209182015b82811115610a1f578254825591600101919060010190610a04565b50610a2b929150610a89565b5090565b828054828255906000526020600020908101928215610a1f579160200282015b82811115610a1f578251825591602001919060010190610a4f565b604051806101400160405280600a906020820280368337509192915050565b610aa391905b80821115610a2b5760008155600101610a8f565b9056fea264697066735822122061756850fb0421516bc6b91b275641e14c48d4e8257d9f84f847f037ef01312d64736f6c63430006080033";

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

    public RemoteFunctionCall<Tuple4<List<BigInteger>, List<BigInteger>, List<BigInteger>, List<BigInteger>>> UserGetData(BigInteger _myID, BigInteger _num) {
        final Function function = new Function(FUNC_USERGETDATA, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_num)), 
                Arrays.<TypeReference<?>>asList(new TypeReference<StaticArray10<Uint256>>() {}, new TypeReference<DynamicArray<Int256>>() {}, new TypeReference<DynamicArray<Int256>>() {}, new TypeReference<DynamicArray<Int256>>() {}));
        return new RemoteFunctionCall<Tuple4<List<BigInteger>, List<BigInteger>, List<BigInteger>, List<BigInteger>>>(function,
                new Callable<Tuple4<List<BigInteger>, List<BigInteger>, List<BigInteger>, List<BigInteger>>>() {
                    @Override
                    public Tuple4<List<BigInteger>, List<BigInteger>, List<BigInteger>, List<BigInteger>> call() throws Exception {
                        List<Type> results = executeCallMultipleValueReturn(function);
                        return new Tuple4<List<BigInteger>, List<BigInteger>, List<BigInteger>, List<BigInteger>>(
                                convertToNative((List<Uint256>) results.get(0).getValue()), 
                                convertToNative((List<Int256>) results.get(1).getValue()), 
                                convertToNative((List<Int256>) results.get(2).getValue()), 
                                convertToNative((List<Int256>) results.get(3).getValue()));
                    }
                });
    }

    public RemoteFunctionCall<TransactionReceipt> UserRegistData(BigInteger _myID, BigInteger _time, BigInteger _lat, BigInteger _lon, List<BigInteger> _accel_x, List<BigInteger> _accel_y, List<BigInteger> _accel_z) {
        final Function function = new Function(
                FUNC_USERREGISTDATA, 
                Arrays.<Type>asList(new org.web3j.abi.datatypes.generated.Uint256(_myID), 
                new org.web3j.abi.datatypes.generated.Uint256(_time), 
                new org.web3j.abi.datatypes.generated.Uint256(_lat), 
                new org.web3j.abi.datatypes.generated.Uint256(_lon), 
                new org.web3j.abi.datatypes.DynamicArray<org.web3j.abi.datatypes.generated.Int256>(
                        org.web3j.abi.datatypes.generated.Int256.class,
                        org.web3j.abi.Utils.typeMap(_accel_x, org.web3j.abi.datatypes.generated.Int256.class)), 
                new org.web3j.abi.datatypes.DynamicArray<org.web3j.abi.datatypes.generated.Int256>(
                        org.web3j.abi.datatypes.generated.Int256.class,
                        org.web3j.abi.Utils.typeMap(_accel_y, org.web3j.abi.datatypes.generated.Int256.class)), 
                new org.web3j.abi.datatypes.DynamicArray<org.web3j.abi.datatypes.generated.Int256>(
                        org.web3j.abi.datatypes.generated.Int256.class,
                        org.web3j.abi.Utils.typeMap(_accel_z, org.web3j.abi.datatypes.generated.Int256.class))), 
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
