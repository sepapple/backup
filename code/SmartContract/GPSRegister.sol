pragma solidity ^0.5.0;

contract GPSRegister{
    
    struct Data{
        uint time;
        uint lat;
        uint lon;
    }
    
    Data[] public Datas;
    
    function DataSet(uint _time, uint _lat, uint _lon) public {
        Datas.push(Data(_time,_lat,_lon));
    }

    function getDataByOwner() public view returns(uint[] memory _time ,uint[] memory _lat ,uint[] memory _lon){
        uint[] memory return_time = new uint[](Datas.length);
        uint[] memory return_lat = new uint[](Datas.length);
        uint[] memory return_lon = new uint[](Datas.length);

        for (uint i = 0; i < Datas.length; i++){
            return_time[i] = Datas[i].time;
            return_lat[i] = Datas[i].lat;
            return_lon[i] = Datas[i].lon;
        }
        
        return (return_time,return_lat,return_lon);

    }

}

