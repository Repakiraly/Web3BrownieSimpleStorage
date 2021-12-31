// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.8.11;
pragma experimental ABIEncoderV2;

contract SimpleStorage {
    // this will get initialized to 0!
    uint256 favNum;

    struct People {
        uint256 favouriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavNum;

    People public person = People({favouriteNumber: 13, name: "Bence"});

    function store(uint256 _favNumber) public {
        favNum = _favNumber;
    }

    //view, pure - no transactions!!!
    function retrieve() public view returns (uint256) {
        return favNum;
    }

    function math(uint256 _favNumber) public pure returns (uint256) {
        _favNumber += _favNumber;
        return _favNumber;
    }

    function seePerson() public view returns (People memory) {
        return person;
    }

    function addPerson(string memory _name, uint256 _favNum) public {
        people.push(People({favouriteNumber: _favNum, name: _name}));
        nameToFavNum[_name] = _favNum;
    }
}
