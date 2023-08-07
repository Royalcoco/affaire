<!DOCTYPE html>
<html>
<head>
    <title>Token Miner</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        var miningInterval;

        function startMining() {
            miningInterval = setInterval(function() {
                mineToken();
            }, 1000); // Mine un token toutes les secondes (ajustez selon vos besoins)
        }

        function stopMining() {
            clearInterval(miningInterval);
        }

        function mineToken() {
            // Ici, vous pouvez ajouter la logique de minage de votre token
            // Par exemple, vous pouvez effectuer une requête AJAX pour communiquer avec un serveur et recevoir les tokens minés

            // Exemple de code pour effectuer une requête AJAX en utilisant jQuery
            $.ajax({
                url: "votre_endpoint_de_minage",
                method: "POST",
                success: function(response) {
                    console.log("Token mined:", response);
                    // Vous pouvez traiter la réponse ici, par exemple, mettre à jour le solde du mineur sur la page
                },
                error: function(xhr, status, error) {
                    console.error("Erreur de minage:", error);
                }
            });
        }
    </script>
</head>
<body>
    <h1>Token Miner</h1>
    <button onclick="startMining()">Start Mining</button>
    <button onclick="stopMining()">Stop Mining</button>
</body>
</html>


contract MyNFT is ERC1088 {
    uint256 private tokenIdCounter;
    mapping(uint256 => string) private tokenURIs;

    constructor() ERC1088 ("MyNFT", "NFT") {}

    function createNFT(address to, string memory tokenURI) external returns (uint256) {
        uint256 tokenId = tokenIdCounter;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        tokenIdCounter++;
        return tokenId;
    }

    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        tokenURIs[tokenId] = tokenURI;
    }

    function tokenURI(uint256 tokenId) public view returns (string memory) {
        return tokenURIs[tokenId];
    }
}
pragma solidity ^0.4.24;

contract NFT {
    struct Token {
        string uri;
        address owner;
    }

    mapping(uint256 => Token) private tokens;
    uint256 private tokenIdCounter;

    event NFTCreated(uint256 tokenId, address owner, string uri);

    function createNFT(address to, string memory tokenURI) external returns (uint256) {
        uint256 tokenId = tokenIdCounter;
        Token memory newToken = Token(tokenURI, to);
        tokens[tokenId] = newToken;
        tokenIdCounter++;

        emit NFTCreated(tokenId, to, tokenURI);

        return tokenId;
    }

    function getTokenURI(uint256 tokenId) external view returns (string memory) {
        require(tokenId < tokenIdCounter, "Invalid token ID");
        return tokens[tokenId].uri;
    }

    function getTokenOwner(uint256 tokenId) external view returns (address) {
        require(tokenId < tokenIdCounter, "Invalid token ID");
        return tokens[tokenId].owner;
    }
}

 function stopMining() {
            clearInterval(miningInterval);
        }

        function mineToken() {
            // Ici, vous pouvez ajouter la logique de minage de votre token
            // Par exemple, vous pouvez effectuer une requête AJAX pour communiquer avec un serveur et recevoir les tokens minés

            // Exemple de code pour effectuer une requête AJAX en utilisant jQuery
            $.ajax({
                url: "votre_endpoint_de_minage",
                method: "POST",
                success: function(response) {
                    console.log("Token mined:", response);
                    // Vous pouvez traiter la réponse ici, par exemple, mettre à jour le solde du mineur sur la page
                },
                error: function(xhr, status, error) {
                    console.error("Erreur de minage:", error);
                }
            });
        }
    </script>
pragma solidity ^0.4.24;

// Path: pragma solidity ^0.8.sol

pragma solidity ^0.4.24;

contract MyNFT is ERC1088 {
    uint256 private tokenIdCounter;
    mapping(uint256 => string) private tokenURIs;

    constructor() ERC1088 ("MyNFT", "NFT") {}

    function createNFT(address to, string memory tokenURI) external returns (uint256) {
        uint256 tokenId = tokenIdCounter;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        tokenIdCounter++;
        return tokenId;
    }

    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        tokenURIs[tokenId] = tokenURI;
    }

    function tokenURI(uint256 tokenId) public view returns (string memory) {
        return tokenURIs[tokenId];
    }
}
```

## 3.2.2. ERC-721

ERC-721 is a standard for representing non-fungible tokens, that is, tokens that are unique and not interchangeable. The standard defines a set of functions that allow you to manage the tokens, such as transferring them between addresses or getting the owner of a token.

The standard is defined in the [EIP-721](https://eips.ethereum.org/EIPS/eip-721) document.

###

import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Exemple d'utilisation
blockchain = Blockchain()
blockchain.add_block(Block(1, time.time(), "Transaction 1", ""))
blockchain.add_block(Block(2, time.time(), "Transaction 2", ""))
blockchain.add_block(Block(3, time.time(), "Transaction 3", ""))

for block in blockchain.chain:
    print("Block #{}:".format(block.index))
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print()

import "./ERC721.sol"; ERC721 private nftContract;

def FIELDNAME = models.DurationField()
def FIELDNAME = models.DurationField()
def FIELDNAME = models.DurationField()
def FIELDNAME = models.DurationField()
def FIELDNAME = models.DurationField()
mean = lambda x: sum(x) / len(x)

constructor(address nftAddress) public {
    nftContract = ERC721(nftAddress);
}

function mine_block(bytes32 previousBlockHash, bytes32[] memory transactions, uint256 difficulty) public {
    uint256 nonce = 0;
    bytes32 currentBlockHash = calculate_hash(previousBlockHash, transactions, nonce);
    while (!is_valid_hash(currentBlockHash, difficulty)) {
        nonce++;
        currentBlockHash = calculate_hash(previousBlockHash, transactions, nonce);
    }

    // Récompense de minage : création d'une NFT unique
    string memory nftURI = bytes32ToString(currentBlockHash);
    uint256 tokenId = nftContract.createNFT(msg.sender, nftURI);

    // Autres opérations de mise à jour de la blockchain
    // ...

    // Émettre un événement pour informer les utilisateurs de la création de la NFT
    emit NFTMined(tokenId, msg.sender, nftURI);
}

function calculate_hash(bytes32 previousBlockHash, bytes32[] memory transactions, uint256 nonce) public pure returns (bytes32) {
    return keccak256(abi.encodePacked(previousBlockHash, transactions, nonce));
}
###

###

class NFT:
    def __init__(self, token_id, owner, metadata):
        self.token_id = token_id
        self.owner = owner
        self.metadata = metadata

class NFTCollection:
    def __init__(self, name):
        self.name = name
        self.nfts = []

    def create_nft(self, token_id, owner, metadata):
        nft = NFT(token_id, owner, metadata)
        self.nfts.append(nft)
        print(f"Created NFT with ID: {token_id}")

    def transfer_nft(self, sender, receiver, token_id):
        for nft in self.nfts:
            if nft.token_id == token_id and nft.owner == sender:
                nft.owner = receiver
                print(f"Transferred NFT with ID: {token_id} from {sender} to {receiver}")
                return
        print(f"Transfer failed. NFT with ID: {token_id} not found or sender mismatch")

# Exemple d'utilisation

# Création d'une nouvelle collection de NFTs
my_collection = NFTCollection("My NFT Collection")

# Création d'un NFT
my_collection.create_nft(1, "Alice", "metadata1")
my_collection.create_nft(2, "Alice", "metadata2")
my_collection.create_nft(3, "Bob", "metadata3")

# Transfert de NFTs entre utilisateurs
my_collection.transfer_nft("Alice", "Bob", 1)
my_collection.transfer_nft("Alice", "Eve", 2)
my_collection.transfer_nft("Bob", "Alice", 3)

