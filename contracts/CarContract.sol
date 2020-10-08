pragma solidity >=0.4.21 <0.7.0;

contract CarContract{
    
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
    
    mapping(uint => ServiceStruct[]) CarInfo;
    mapping(uint => ServiceStruct) Car;
    
    function CarStart(uint _myID,uint _PartnerID,uint _time,uint _ConnectionID) public {
        Car[_myID].myID = _myID;
        Car[_myID].PartnerID = _PartnerID;
        Car[_myID].start_time = _time;
        Car[_myID].ConnectionID = _ConnectionID;
        Car[_myID].start_block = block.number;
        Car[_myID].owner = msg.sender;
    }
    
    function CarRegistData(uint _myID,uint _time, uint _lat, uint _lon,int[] memory _accel_x,int[] memory _accel_y,int[] memory _accel_z) public {
        require(Car[_myID].owner == msg.sender);
        Car[_myID].myID = _myID;
        Car[_myID].time = _time;
        Car[_myID].lat = _lat;
        Car[_myID].lon = _lon;
        Car[_myID].accel_x = _accel_x;
        Car[_myID].accel_y = _accel_y;
        Car[_myID].accel_z = _accel_z;
    }

    
    function CarFinish(uint _myID,uint _time) public{
        require(Car[_myID].owner == msg.sender);
        Car[_myID].finish_time = _time;
        Car[_myID].finish_block = block.number;
        CarInfo[_myID].push(Car[_myID]);
        Car[_myID].owner = address(0);
    }
    

   function CarGetData(uint _myID,uint _num) public view returns(uint[10] memory ret_array,int[] memory ret_accel_x,int[] memory ret_accel_y,int[] memory ret_accel_z){
       ret_array[0] = CarInfo[_myID][_num].myID;
       ret_array[1] = CarInfo[_myID][_num].time;
       ret_array[2] = CarInfo[_myID][_num].lat;
       ret_array[3] = CarInfo[_myID][_num].lon;
       ret_accel_x = CarInfo[_myID][_num].accel_x;
       ret_accel_y = CarInfo[_myID][_num].accel_y;
       ret_accel_z = CarInfo[_myID][_num].accel_z;
       ret_array[4] = CarInfo[_myID][_num].start_time;
       ret_array[5] = CarInfo[_myID][_num].finish_time;
       ret_array[6] = CarInfo[_myID][_num].start_block;
       ret_array[7] = CarInfo[_myID][_num].finish_block;
       ret_array[8]= CarInfo[_myID][_num].PartnerID;
       ret_array[9]= CarInfo[_myID][_num].ConnectionID;
    }
}

