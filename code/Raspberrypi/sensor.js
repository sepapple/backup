const imu = require("node-sense-hat").Imu;

const IMU = new imu.IMU();

IMU.getValue((err,data) => {
    if (err != null) {
        console.error("Could not read sensor data: ", err);
        return;
    }

    console.log("Accelleration is: ", JSON.stringify(data.accel, null, "  "));
    console.log("Gyroscope is: ", JSON.stringify(data.gyro, null, "  "));
});


