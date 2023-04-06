pragma solidity ^0.8.0;

contract IPFSVote {
    // Struct to store vote information
    struct Vote {
        string ipfsHash;    // IPFS hash value of the vote information
        uint256 count;      // Vote count
    }

    mapping (address => bool) public voters;  // Mapping to store voter information
    mapping (uint256 => Vote) public votes;   // Mapping to store vote information

    uint256 public voteCount = 0;  // Total vote count

    // Function to allow voters to cast their vote
    function vote(string memory ipfsHash) public {
        // Check if the voter has already voted
        require(!voters[msg.sender], "You have already voted!");
        voters[msg.sender] = true;

        // Increase the total vote count and store the vote information
        voteCount += 1;
        votes[voteCount] = Vote(ipfsHash, 1);
    }

    // Function to retrieve the vote information
    function getVote(uint256 voteId) public view returns (string memory, uint256) {
        // Check if the vote ID is valid
        require(voteId <= voteCount && voteId > 0, "Invalid vote ID!");
        Vote storage vote = votes[voteId];

        // Return the vote information and count
        return (vote.ipfsHash, vote.count);
    }
}
