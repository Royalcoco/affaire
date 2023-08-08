import _hashlib
from . import utils
def get_sha1(filename):
    sha = hashlib.new('ripemd160')
    with open (filename, 'rb') as f:
        while True :
            data=f.read()
            if not len(data) > 0:
                break;
            sha.update(data);
            return sha
        .hexdigest();
        <KEY>
        class Blockchain():
            def __init__(self,*args,**kwargs):
                self._blocks=[]
                self.__dict__.update(*args,**kwargs)
                @property
                def blocks(self):
                    return self._blocks
                def addBlock(self,_block):
                    self._blocks.append(_block)
                    print("added block")
                    def getLastBlockHash(self):
                        last_block=_blocks[-1]
                        hash_=last_block['hash']
                        return hash_;
                    def proofOfWork(self,lastProof):
                        newproof=0
                        check=False
                        while not check:
                            testproof=(str(lastProof**2)+str(lastProof)).encode().decode('
                                                                                         utf-8');
                            #print(testproof)
                            if int(utils.getSHA1(testproof))%5==0:
                                check=True
                            else:
                                
                                lastProof+=1
                                return str(lastProof).encode().decode('utf-8');
                            return str(newproof).encode().decode('utf-8');
                        
                        def createGenesisBlock(self):
                            genesis_block={
                                "index":'0',
                                "timestamp":"",
                                "transactions":[],
                                "nonce":'',
                                "previoushash":''}
                            return genesis_block
                        ;
                        
                        def getBlockchain(self):
                            blockchain=[genesis_block];
                            for i in range (len(blockchain)):
                                _block=blockchain[i]
                                previoushash=getBlockLastHash()
                                nonce=proofOfWork(previoushash)
                                transactions=createTransactions()
                                timestamp=time.strftime("%Y-%m-%d %H:%M:%S");
                                index=int(i+1);
                                _block["index"]=index;
                                _block["timestamp"]=timestamp;
                                _block["transactions"]=transactions;
                                _block["nonce"]=nonce;
                                _block["previoushash"]=previoushash;
                                blockchain.append(_block);
                                return blockchain
                            
        #include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <openssl/sha.h>

class Block {
public:
    int index;
    std::string previous_hash;
    time_t timestamp;
    std::string data;
    std::string hash;

    Block(int idx, const std::string& prev_hash, time_t time, const std::string& d, const std::string& h)
        : index(idx), previous_hash(prev_hash), timestamp(time), data(d), hash(h) {}
};

std::string calculate_hash(int index, const std::string& prev_hash, time_t timestamp, const std::string& data) {
    std::string value = std::to_string(index) + prev_hash + std::to_string(timestamp) + data;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((const unsigned char*)value.c_str(), value.length(), hash);

    std::string hash_str;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        hash_str += hash[i];
    }
    return hash_str;
}

Block create_genesis_block() {
    time_t now = time(0);
    return Block(0, "0", now, "Genesis Block", calculate_hash(0, "0", now, "Genesis Block"));
}

Block create_new_block(const Block& previous_block, const std::string& data) {
    int index = previous_block.index + 1;
    time_t timestamp = time(0);
    std::string hash = calculate_hash(index, previous_block.hash, timestamp, data);
    return Block(index, previous_block.hash, timestamp, data, hash);
}

int main() {
    std::vector<Block> blockchain;
    blockchain.push_back(create_genesis_block());
    Block previous_block = blockchain[0];

    // Test getting data from a URL
    std::string data = "data fetched from URL";  // Replace this with actual data fetching logic
    Block new_block = create_new_block(previous_block, data);
    blockchain.push_back(new_block);
    previous_block = new_block;

    // Print the blockchain
    for (const Block& block : blockchain) {
        std::cout << "Block " << block.index << " - Hash: " << block.hash << std::endl;
    }

    return 0;
}