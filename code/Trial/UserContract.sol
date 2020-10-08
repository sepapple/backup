pragma solidity >=0.4.21 <0.7.0;

contract UserContract{
    
    struct ServiceStruct{
        uint myID;
        uint time;
        uint lat;
        uint lon;
        int[] accel_x;
        int[] accel_y;
        int[] accel_z;
        uint start_time;
        uint finish_time;
        uint start_block;
        uint finish_block;
        uint PartnerID;
        uint ConnectionID;
    }
    
    mapping(uint => ServiceStruct[]) UserInfo;
    mapping(uint => ServiceStruct[]) CarInfo;
    mapping(uint => ServiceStruct) User;
    mapping(uint => ServiceStruct) Car;
    mapping(uint => boolean) 

    function UserStart(uint _myID,uint _PartnerID,uint _time,uint _ConnectionID) public {
        User[_myID].myID = _myID;
        User[_myID].PartnerID = _PartnerID;
        User[_myID].start_time = _time;
        User[_myID].ConnectionID = _ConnectionID;
        User[_myID].start_block = block.number;
    }
    
    function CarStart(uint _myID,uint _PartnerID,uint _time,uint _ConnectionID) public {
        Car[_myID].myID = _myID;
        Car[_myID].PartnerID = _PartnerID;
        Car[_myID].start_time = _time;
        Car[_myID].ConnectionID = _ConnectionID;
        Car[_myID].start_block = block.number;
    }
    function UserRegistData(uint _myID,uint _time, uint _lat, uint _lon,int[] memory _accel_x,int[] memory _accel_y,int[] memory _accel_z) public {
        User[_myID].myID = _myID;
        User[_myID].time = _time;
        User[_myID].lat = _lat;
        User[_myID].lon = _lon;
        User[_myID].accel_x = _accel_x;
        User[_myID].accel_y = _accel_y;
        User[_myID].accel_z = _accel_z;
    }
    
    function CarRegistData(uint _myID,uint _time, uint _lat, uint _lon,int[] memory _accel_x,int[] memory _accel_y,int[] memory _accel_z) public {
        Car[_myID].myID = _myID;
        Car[_myID].time = _time;
        Car[_myID].lat = _lat;
        Car[_myID].lon = _lon;
        Car[_myID].accel_x = _accel_x;
        Car[_myID].accel_y = _accel_y;
        Car[_myID].accel_z = _accel_z;
    }

    function UserFinish(uint _myID,uint _time) public{
        User[_myID].finish_time = _time;
        User[_myID].finish_block = block.number;
        UserInfo[_myID].push(User[_myID]);
    }
    
    function CarFinish(uint _myID,uint _time) public{
        Car[_myID].finish_time = _time;
        Car[_myID].finish_block = block.number;
        CarInfo[_myID].push(Car[_myID]);
    }
    
   function UserGetData(uint _myID) public view returns(uint[10] memory ret_array,int[] memory ret_accel_x,int[] memory ret_accel_y,int[] memory ret_accel_z){
       ret_array[0] = UserInfo[_myID][0].myID;
       ret_array[1] = UserInfo[_myID][0].time;
       ret_array[2] = UserInfo[_myID][0].lat;
       ret_array[3] = UserInfo[_myID][0].lon;
       ret_accel_x = UserInfo[_myID][0].accel_x;
       ret_accel_y = UserInfo[_myID][0].accel_y;
       ret_accel_z = UserInfo[_myID][0].accel_z;
       ret_array[4] = UserInfo[_myID][0].start_time;
       ret_array[5] = UserInfo[_myID][0].finish_time;
       ret_array[6] = UserInfo[_myID][0].start_block;
       ret_array[7] = UserInfo[_myID][0].finish_block;
       ret_array[8]= UserInfo[_myID][0].PartnerID;
       ret_array[9]= UserInfo[_myID][0].ConnectionID;
    }
}

