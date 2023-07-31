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

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Télécharger les ressources nécessaires pour NLTK
nltk.download('punkt')
nltk.download('stopwords')

def describe_procedure(user_input):
    # Prétraitement du texte
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

    # Génération de la description de la procédure
    description = "La procédure à suivre est la suivante : "

    # Ajoutez ici votre logique pour générer la description en fonction de l'entrée utilisateur

    return description

def main():
    while True:
        user_input = input("Entrez votre commande : ")

        if user_input.lower() == "exit":
            break

        description = describe_procedure(user_input)
        print(description)

if __name__ == '__main__':
    main()
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

