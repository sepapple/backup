pragma solidity >=0.4.21 <0.7.0;

contract UserContract{
    
    struct ServiceStruct{
        uint myID;
        uint PartnerID;
        uint ConnectionID;
        address owner;
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
    }
    
    mapping(uint => ServiceStruct[]) UserInfo;
    mapping(uint => ServiceStruct) User;

    function UserStart(uint _myID,uint _PartnerID,uint _time,uint _ConnectionID) public {
        User[_myID].myID = _myID;
        User[_myID].PartnerID = _PartnerID;
        User[_myID].start_time = _time;
        User[_myID].ConnectionID = _ConnectionID;
        User[_myID].start_block = block.number;
        User[_myID].owner= msg.sender;
    }
    
    function UserRegistData(uint _myID,uint _time, uint _lat, uint _lon,int[] memory _accel_x,int[] memory _accel_y,int[] memory _accel_z) public {
        require(User[_myID].owner == msg.sender);
        User[_myID].myID = _myID;
        User[_myID].time = _time;
        User[_myID].lat = _lat;
        User[_myID].lon = _lon;
        User[_myID].accel_x = _accel_x;
        User[_myID].accel_y = _accel_y;
        User[_myID].accel_z = _accel_z;
    }
    

    function UserFinish(uint _myID,uint _time) public{
        require(User[_myID].owner == msg.sender);
        User[_myID].finish_time = _time;
        User[_myID].finish_block = block.number;
        UserInfo[_myID].push(User[_myID]);
        User[_myID].owner = address(0);
    }
    
   function UserGetData(uint _myID,uint _num) public view returns(uint[10] memory ret_array,int[] memory ret_accel_x,int[] memory ret_accel_y,int[] memory ret_accel_z){
       ret_array[0] = UserInfo[_myID][_num].myID;
       ret_array[1] = UserInfo[_myID][_num].time;
       ret_array[2] = UserInfo[_myID][_num].lat;
       ret_array[3] = UserInfo[_myID][_num].lon;
       ret_accel_x = UserInfo[_myID][_num].accel_x;
       ret_accel_y = UserInfo[_myID][_num].accel_y;
       ret_accel_z = UserInfo[_myID][_num].accel_z;
       ret_array[4] = UserInfo[_myID][_num].start_time;
       ret_array[5] = UserInfo[_myID][_num].finish_time;
       ret_array[6] = UserInfo[_myID][_num].start_block;
       ret_array[7] = UserInfo[_myID][_num].finish_block;
       ret_array[8]= UserInfo[_myID][_num].PartnerID;
       ret_array[9]= UserInfo[_myID][_num].ConnectionID;
    }
    
}

