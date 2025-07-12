import hashlib
import time

def proof_of_work(block, difficulty):
    """
    Find a nonce that, when hashed with the block data, results in a hash
    that meets the given difficulty criteria (leading zeros).
    """
    nonce = 0
    while True:
        data = str(block) + str(nonce)
        hash_result = hashlib.sha256(data.encode()).hexdigest()
        if hash_result.startswith('0' * difficulty):
            return nonce, hash_result
        nonce += 1

def validate_proof(block, nonce, difficulty):
    """
    Validates if the given nonce, when hashed with the block data,
    meets the difficulty criteria.
    """
    data = str(block) + str(nonce)
    hash_result = hashlib.sha256(data.encode()).hexdigest()
    return hash_result.startswith('0' * difficulty)

if __name__ == '__main__':
    block_data = "This is a sample block data"
    difficulty = 4  # Number of leading zeros required in the hash
   
    start_time = time.time()
    nonce, hash_result = proof_of_work(block_data, difficulty)
    end_time = time.time()
    print(f"Block Data: {block_data}")
    print(f"Nonce: {nonce}")
    print(f"Hash Result: {hash_result}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
   
    if validate_proof(block_data, nonce, difficulty):
        print("Proof of work is valid!")
    else:
        print("Proof of work is invalid!")
class Block:
    def __init__(self, data, previous_hash):
        """
        Initializes a new Block object with
        the given data and previous hash.
        """
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculates the SHA-256 hash of the
        block's data, previous hash, and nonce.
        """
        sha = hashlib.sha256()
        sha.update(str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty):
        """
        Mines the block using the Proof-of-Work algorithm
        with the given difficulty level.
        """
        while self.hash[0:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined:", self.hash)

class Blockchain:
    def __init__(self):
        """
        Initializes a new Blockchain object with
        a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block of the blockchain with
        arbitrary data and a previous hash of "0".
        """
        return Block("Genesis Block", "0")

    def add_block(self, new_block):
        """
        Adds a new block to the blockchain with
        the given data.
        """
        new_block.previous_hash = self.chain[-1].hash
       
        # Difficulty level of 4
        new_block.mine_block(4) 
        self.chain.append(new_block)

# create a new blockchain
blockchain = Blockchain()

# create and add three blocks to the blockchain
block1 = Block("Transaction data 1", "")
blockchain.add_block(block1)

block2 = Block("Transaction data 2", "")
blockchain.add_block(block2)

block3 = Block("Transaction data 3", "")
blockchain.add_block(block3) 
