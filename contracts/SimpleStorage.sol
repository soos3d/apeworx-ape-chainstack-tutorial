// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    string storedWord;

    function setWord(string memory _word) public {
        storedWord = _word;
    }

    function getWord() public view returns (string memory) {
        return storedWord;
    }
}
