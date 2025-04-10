import hashlib
import time


class Block: 
    def __init__(self,index,previous_hash,data,timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}".encode()
        return hashlib.sha256(block_string).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self): 
        return Block(0, "0", "Blok geneze")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


blockchain = Blockchain()

blockchain.add_block(Block(1, blockchain.get_latest_block().hash,"Blok 1 Podaci"))
blockchain.add_block(Block(2, blockchain.get_latest_block().hash,"Blok 2 Podaci"))

for block in blockchain.chain: 
    print("Block: ", block.index)
    print("Timestamp: ", block.timestamp)
    print("Data: ", block.data)
    print("Hash: ", block.hash)
    print("Previous hash: ", block.previous_hash, "\n")
