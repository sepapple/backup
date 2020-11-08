package com.example.trial;

import android.Manifest;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothGatt;
import android.bluetooth.BluetoothGattCallback;
import android.bluetooth.BluetoothGattCharacteristic;
import android.bluetooth.BluetoothGattDescriptor;
import android.bluetooth.BluetoothGattService;
import android.bluetooth.BluetoothManager;
import android.bluetooth.BluetoothProfile;
import android.bluetooth.le.BluetoothLeScanner;
import android.bluetooth.le.ScanCallback;
import android.bluetooth.le.ScanResult;
import android.content.Context;
import android.content.pm.PackageManager;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.view.WindowManager;
import android.widget.TextView;
import android.os.Handler;
import android.os.Looper;
import org.json.JSONException;
import org.web3j.crypto.Credentials;
import org.web3j.protocol.admin.Admin;
import org.web3j.protocol.core.methods.response.TransactionReceipt;
import org.web3j.protocol.http.HttpService;
import org.web3j.tx.gas.DefaultGasProvider;
import org.web3j.tx.gas.StaticGasProvider;

//測位に関係があるパッケージ
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.content.Context;

import java.math.BigInteger;
import java.util.List;
import java.util.UUID;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements SensorEventListener,LocationListener{

    // 接続対象となるペリフェラルの名前(XXXXは学籍番号の下4桁)
    private static final String PERIPHERAL_NAME = "Raspberry-pi";

    // 接続対象となるサービスのUUID.
    private static final String SERVICE_UUID = "19B10010-E8F2-537E-4F6C-D104768A1214";

    // 接続対象となるキャラクタリスティックのUUID.
    private static final String CHAR_WRITE_UUID = "19B10011-E8F2-537E-4F6C-D104768A1214";
    //private static final String CHAR_WRITE_UUID = "19B10012-E8F2-537E-4F6C-D104768A1214";
    private static final String CHAR_NOTIFY_UUID = "19B10012-E8F2-537E-4F6C-D104768A1214";

    // キャラクタリスティック設定UUID(固定値).
    private static final String NOTIFY_CHARACTERISTIC_CONFIG_UUID = "00002902-0000-1000-8000-00805f9b34fb";
    // ペリフェラルと接続しない: 0, ペリフェラルと接続する: 1
    private int flag_connect = 1;

    // AndroidのID
    private static final String ANDROID_ID = "100";

    //ラズパイIDとコネクションID
    private static String[] ID;

    //送信する位置情報
    BigInteger lat = new BigInteger("0");
    BigInteger lon = new BigInteger("0");

    //加速度に関連する変数
    int counter = 0;
    long last_time = 0;
    long current_time =0;
    private static final int ALLAY_NUM = 10; //配列に入れる数
    private static final int MEASURE_MILL = 100; //0.1秒間隔で計測
    List<BigInteger> SendAccel_x = new ArrayList<BigInteger>();
    List<BigInteger> SendAccel_y = new ArrayList<BigInteger>();
    List<BigInteger> SendAccel_z = new ArrayList<BigInteger>();
    List<BigInteger> TempAccel_x = new ArrayList<BigInteger>();
    List<BigInteger> TempAccel_y = new ArrayList<BigInteger>();
    List<BigInteger> TempAccel_z = new ArrayList<BigInteger>();

    //スマートコントラクトを制御するフラグと時間
    private boolean connect_flag = false;
    private boolean start_flag = false;
    //private boolean regist_flag = false;
    long last_send = 0;
    long current_send =0;
    private static final int TRANSMISSION_INTERVAL = 1000; //2秒間隔で送信


    //センサマネージャを定義
    private SensorManager sensor_manager;

    //ロケーションマネージャーを定義
    private LocationManager location_manager;

    //センサーから届いた値を格納する配列を定義
    private float[] sensor_values = new float[3];
    final Handler mainHandler = new Handler(Looper.getMainLooper());

    // BLEで利用するクラス群
    private BluetoothManager mBleManager;
    private BluetoothAdapter mBleAdapter;
    private BluetoothLeScanner mBleScanner;
    private BluetoothGatt mBleGatt;
    private BluetoothGattCharacteristic notifyCharacteristic, writeCharacteristic;

    TextView textbox;

    private final static String BR=System.getProperty("line.separator");

    //ブロックチェーンで使用
    Admin web3j = Admin.build(new HttpService("http://192.168.30.30:8545"));
    //String contractaddress = "0xb6b8c9e8cb0be9fe2938b3c066d4764146fb304c";
    String contractAddress = "0x109D0C94E2854791Cb83122bdDFb293dC096475a";
    //Credentials credentials = Credentials.create("0x5e14304f6676c27587c0d8f4c40ed1e22bc6eb43d6d27063a860802d294685e8");  //資格情報
    Credentials credentials = Credentials.create("80dfbd85ae71c59a5a90ac799f8500a457a924aa613184db0d479843317fc4f3");  //資格情報
    UserContract myContract = UserContract.load(contractAddress,web3j,credentials,new DefaultGasProvider());
    //UserContract myContract = UserContract.load(contractAddress,web3j,credentials,new StaticGasProvider(BigInteger.valueOf(40000000000L),BigInteger.valueOf(4000000L)));

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle("Trial");
        textbox = (TextView) findViewById(R.id.textbox);



        // アプリ実行中はスリープしない
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);


        // Bluetoothの使用準備.
        mBleManager = (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);
        mBleAdapter = mBleManager.getAdapter();

        //センサーを制御するための変数の初期化
        sensor_manager = (SensorManager)getSystemService(Context.SENSOR_SERVICE);
        // ロケーションマネージャの取得
        location_manager=(LocationManager)getSystemService(Context.LOCATION_SERVICE);

        //センサーの値を管理するスレッドの起動
        SensorValue();

    }

    @Override
    protected void onResume() {
        super.onResume();
        // *************************************************** //
        // Bluetooth関連の処理                                  //
        // *************************************************** //

        // 位置情報の利用許可を利用者に求める (BLEも位置情報として利用できるため，許可が必要)
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION}, 1);

            return;
        }

        // BLEが使用可能なら、通信相手をスキャン
        if ((mBleAdapter != null) || (mBleAdapter.isEnabled())) {
            mBleScanner = mBleAdapter.getBluetoothLeScanner();
            mBleScanner.startScan(scanCallback);
        }

        //情報を取得するセンサーの設定
        List<Sensor> sensors = sensor_manager.getSensorList(Sensor.TYPE_ACCELEROMETER);
        Sensor sensor = sensors.get(0);

        //センサーからの情報を取得開始
        sensor_manager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_UI);

        // ロケーションマネージャの設定 - 測位方法を指定して測位を開始
        location_manager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, this);
    }

    Runnable ShowReceiveParamater = new Runnable() {
        @Override
        public void run() {
            long time = System.currentTimeMillis()/1000;
            String text = "AndroidID"+ANDROID_ID+BR+
                    "ラズパイID: " + ID[0]+BR+
                    "コネクションID"+ ID[1]+BR+
                    "時間" + time+BR+
                    "緯度: " + lat+BR+
                    "経度: " + lon+BR+
                    "x軸加速度: " + sensor_values[0]+BR+
                    "y軸加速度" + sensor_values[1]+BR+
                    "z軸加速度" + sensor_values[2]+BR;
            textbox.setText(text);
            /*
            textbox.append("AndroidID: " + ANDROID_ID+"\n");
            textbox.append("ラズパイID: " + ID[0]+"\n");
            textbox.append("時間" + time+"\n");
            textbox.append("緯度: " + lat+"\n");
            textbox.append("経度: " + lon+"\n");
            textbox.append("x軸加速度: " + sensor_values[0]+"\n");
            textbox.append("y軸加速度" + sensor_values[1]+"\n");
            textbox.append("z軸加速度" + sensor_values[2]+"\n");
             */


        }
    };

    private final BluetoothGattCallback mGattCallback = new BluetoothGattCallback() {
        @Override
        public void onConnectionStateChange(BluetoothGatt gatt, int status, int newState)
        {
            // 接続状況が変化したら実行.
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                // 接続に成功したらサービスを検索する.
                gatt.discoverServices();
            } else if (newState == BluetoothProfile.STATE_DISCONNECTED) {
                // 接続が切れたらGATTを空にする.
                if (mBleGatt != null)
                {
                    //regist_flag = false;
                    connect_flag = false;
                    try {
                        Thread.sleep(2000); // 2秒間だけ処理を止める
                    } catch (InterruptedException e) {
                    }
                    Finish();
                    mBleGatt.close();
                    mBleGatt = null;
                    start_flag = false;
                }
            }
        }

        @Override
        public void onServicesDiscovered(BluetoothGatt gatt, int status)
        {
            String text;
            // Serviceが見つかったら実行.
            if (status == BluetoothGatt.GATT_SUCCESS) {


                // UUIDが同じかどうかを確認する.
                BluetoothGattService service = gatt.getService(UUID.fromString(SERVICE_UUID));
                if (service != null)
                {

                    // 指定したUUIDを持つCharacteristicを確認する.
                    notifyCharacteristic = service.getCharacteristic(UUID.fromString(CHAR_NOTIFY_UUID));
                    writeCharacteristic = service.getCharacteristic(UUID.fromString(CHAR_WRITE_UUID));

                    if (notifyCharacteristic != null) {

                        // Service, CharacteristicのUUIDが同じならBluetoothGattを更新する.
                        mBleGatt = gatt;

                        // キャラクタリスティックが見つかったら、Notificationをリクエスト.
                        boolean notify_registered = mBleGatt.setCharacteristicNotification(notifyCharacteristic, true);

                        // Characteristic の Notificationを有効化する.
                        BluetoothGattDescriptor notify_descriptor = notifyCharacteristic.getDescriptor(
                                UUID.fromString(NOTIFY_CHARACTERISTIC_CONFIG_UUID));


                        notify_descriptor.setValue(BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE);


                        mBleGatt.writeDescriptor(notify_descriptor);

                    }
                }
            }
        }

        @Override
        public void onCharacteristicChanged(BluetoothGatt gatt, BluetoothGattCharacteristic characteristic)
        {

            byte[] recvValue;
            final String text;
            String receive;

            // キャラクタリスティックのUUIDをチェック(getUuidの結果が全て小文字で帰ってくるのでUpperCaseに変換)
            if (CHAR_NOTIFY_UUID.equals(characteristic.getUuid().toString().toUpperCase()))
            {
                //値を取得しbufferからStringへ変換
                recvValue = characteristic.getValue();
                receive =  new String(recvValue);
                ID = receive.split(",",0);
                if(connect_flag == false){
                    connect_flag = true;
                    SmartContract();
                }
                //mainHandler.post(ShowReceiveParamater);
                /*
                if(start_flag == true){
                    start_flag = false;
                    Start();
                    regist_flag = true;
                }
                current_send = System.currentTimeMillis();
                if(regist_flag == true){
                    if(current_send-last_send > TRANSMISSION_INTERVAL) {
                        DataRegist();
                        last_send = current_send;
                    }
                }
                 */

                //logの出力
                text = "BLE Received Value: " + receive;
                Log.d("blelog", text);

                //writeCharacteristicにIDを書き込み
                writeCharacteristic.setValue(ANDROID_ID);
                mBleGatt.writeCharacteristic(writeCharacteristic);

            }
        }
    };

    private ScanCallback scanCallback = new ScanCallback(){
        @Override
        public void onScanResult(int callbackType, ScanResult result) {
            float values;
            super.onScanResult(callbackType, result);

            // 発見したペリフェラルが接続対象と一致する場合には、Rssiを取得
            if((result.getDevice().getName() != null) && (result.getDevice().getName().equals(PERIPHERAL_NAME))){
                values = result.getRssi();

                String text = "Found: " + result.getDevice().getName() + ", " + values;
                Log.d("blelog", text);

                if(flag_connect == 1){
                    result.getDevice().connectGatt(getApplicationContext(), false, mGattCallback);
                }
            }
        }

        @Override
        public void onScanFailed(int intErrorCode) {
            super.onScanFailed(intErrorCode);
        }
    };

    public void onLocationChanged(Location location) {

        String string_lat = String.valueOf(location.getLatitude());
        String string_lon = String.valueOf(location.getLongitude());
        Log.d("blelog", string_lat);
        Log.d("blelog", string_lon);

        int int_lat = (int)(Float.parseFloat(string_lat)*10000000);
        int int_lon = (int)(Float.parseFloat(string_lon)*10000000);
        lat = BigInteger.valueOf(int_lat);
        lon = BigInteger.valueOf(int_lon);
    }

    public void onProviderEnabled(String provider) {
    }

    public void onProviderDisabled(String provider) {
    }

    public void onStatusChanged(String provider, int status,Bundle extras) {

    }

    //センサーイベント受信時に呼ばれるコールバック関数
    public void onSensorChanged(SensorEvent event){
        if(event.sensor.getType() == Sensor.TYPE_ACCELEROMETER){
            sensor_values = event.values.clone();

        }
    }

    //センサーの精度の変更時に呼ばれるコールバック関数
    public void onAccuracyChanged(Sensor sendor, int accuracy){}

    //センサーの値を管理する非同期処理
    public void SensorValue() {
        new Thread(new Runnable() {
            public void run() {
                while(true) {
                    current_time = System.currentTimeMillis();
                    //0.1秒に一回取れるように設定
                    if ((current_time - last_time) > MEASURE_MILL) {
                        TempAccel_x.add(BigInteger.valueOf((int) (sensor_values[0] * 10000000)));
                        TempAccel_y.add(BigInteger.valueOf((int) (sensor_values[1] * 10000000)));
                        TempAccel_z.add(BigInteger.valueOf((int) (sensor_values[2] * 10000000)));
                        last_time = current_time;
                        if (TempAccel_x.size() == ALLAY_NUM) {
                            SendAccel_x = TempAccel_x;
                            SendAccel_y = TempAccel_y;
                            SendAccel_z = TempAccel_z;
                            TempAccel_x = new ArrayList<>();
                            TempAccel_y = new ArrayList<>();
                            TempAccel_z = new ArrayList<>();
                        }
                    }
                }



            }
        }).start();
    }
    //SmartContractを制御するための非同期処理
    public void SmartContract() {
        new Thread(new Runnable() {
            public void run() {
                while(connect_flag == true){
                    if(start_flag == false){
                        start_flag = true;
                        Start();
                        //regist_flag = true;
                    }
                    current_send = System.currentTimeMillis();
                    if(current_send-last_send > TRANSMISSION_INTERVAL) {
                        DataRegist();
                        last_send = current_send;
                    }
                }

            }
        }).start();
    }

    //Start関数の非同期処理
    public void Start() {
        new Thread(new Runnable() {
            public void run() {
                final Handler mainHandler = new Handler(Looper.getMainLooper());

                try {
                    long send_time = System.currentTimeMillis();
                    String text = "AndroidID"+ANDROID_ID+BR+
                            "ラズパイID: " + ID[0]+BR+
                            "コネクションID"+ ID[1]+BR+
                            "時間" + send_time+BR;
                    Log.d("StartData:",text);

                    TransactionReceipt transactionReceipt = myContract.UserStart(new BigInteger(ANDROID_ID)
                            , new BigInteger(ID[0]), BigInteger.valueOf(send_time), new BigInteger(ID[1])).send();
                    Log.d("StartTransaction", transactionReceipt.toString());
                }catch(Exception e){
                    mainHandler.post(()->{
                        textbox.setText(e.toString());
                    });
                    Log.d("Start Error", e.toString());
                }


            }
        }).start();
    }

    //Regist関数の非同期処理
    public void DataRegist() {
        new Thread(new Runnable() {
            public void run() {
                try {
                    long send_time = System.currentTimeMillis();
                    String text = "AndroidID"+ANDROID_ID+BR+
                            "時間" + send_time+BR+
                            "緯度: " + lat+BR+
                            "経度: " + lon+BR+
                            "x軸加速度:" + SendAccel_x+BR+
                            "y軸加速度" + SendAccel_y+BR+
                            "z軸加速度" + SendAccel_z+BR;
                    Log.d("RegistData:",text);
                    mainHandler.post(() -> {
                        textbox.setText(text);
                    });
                    TransactionReceipt transactionReceipt = myContract.UserRegistData(new BigInteger(ANDROID_ID)
                            ,BigInteger.valueOf(send_time),lat,lon,SendAccel_x,SendAccel_y,SendAccel_z).send();


                    Log.d("RegistTransaction", transactionReceipt.toString());
                }catch(Exception e) {
                    mainHandler.post(() -> {
                        textbox.setText(e.toString()); });
                    Log.d("Regist Error",e.toString());
                }


            }
        }).start();
    }

    //Finish関数の非同期処理
    public void Finish(){
        new Thread(new Runnable() {
            public void run() {

                try {
                    long send_time = System.currentTimeMillis();
                    String text = "AndroidID"+ANDROID_ID+BR+
                            "時間" + send_time+BR;
                    Log.d("FinishData:",text);

                    TransactionReceipt transactionReceipt = myContract.UserFinish(new BigInteger(ANDROID_ID)
                            ,BigInteger.valueOf(send_time)).send();
                    Log.d("FinishTransaction", transactionReceipt.toString());
                }catch(Exception e){
                    mainHandler.post(()->{
                        textbox.setText(e.toString());
                    });
                    Log.d("Finish Error", e.toString());
                }


            }
        }).start();
    }

}