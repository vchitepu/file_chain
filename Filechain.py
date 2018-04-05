# Cryptek Security
# FileChain Data Storage
# Developer: Vinay Chitepu


# Imported Modules
import hashlib
import json
import os
from time import time
from uuid import uuid4


class Filechain(object):

	#Initialize the chain
     def __init__(self):
         self.file ={}
         self.chain = []

         # Genesis Block
         self.new_block(previous_hash=1, proof=100)

     #----------------------------------------------------------------------------------------------------#

     # Create a new Block in the chain
     def new_block(self, proof, previous_hash=None):
         # :param proof: <int> The proof given by the Proof of Work algorithm
         # :param previous_hash: (Optional) <str> Hash of previous Block
         # :return: <dict> New Block

         block = {
             'index': len(self.chain) + 1,
             'timestamp': time(),
             'file': self.file,
             'proof': proof,
             'previous_hash': previous_hash or self.hash(self.chain[-1]),
          }

         # Reset the current list of transactions
         self.file = {}

         self.chain.append(block)
         return block

     #----------------------------------------------------------------------------------------------------#

     # Creates a new file to go into the next mined Block
     def new_file(self, file_path):
         # :param file_path: <str> Path of file on host computer
         # :return: <int> The index of the Block that will hold this transaction

         # Uses bash to convert file into hex (xxd format)
         command = 'xxd ' + file_path
         data = os.popen(command).read()

         self.file = {
             'file_path': file_path,
             'data': data
          }

         return self.last_block['index'] + 1

     #----------------------------------------------------------------------------------------------------#

     # Returns the last block of the chain
     @property
     def last_block(self):
        return self.chain[-1]

     #----------------------------------------------------------------------------------------------------#

   	# Creates a SHA-256 hash of a Block
     @staticmethod
     def hash(block):
         # :param block: <dict> Block
         # :return: <str>
        
         # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
         block_str = json.dumps(block, sort_keys=True).encode()
         return hashlib.sha256(block_str).hexdigest()

     #----------------------------------------------------------------------------------------------------#

     # Proof of Work 
     def proof_of_work(self, last_proof):
         # Algorithm:
         #  - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         #  - p is the previous proof, and p' is the new proof

         # :param last_proof: <int> Previous Proof
         # :return: <int> Current Proof

         proof = 0
         while self.valid_proof(last_proof, proof) is False:
             proof += 1

         return proof

     #----------------------------------------------------------------------------------------------------#

     # Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
     @staticmethod
     def valid_proof(last_proof, proof):
         # :param last_proof: <int> Previous Proof
         # :param proof: <int> Current Proof
         # :return: <bool> True if correct, False if not.

         guess = f'{last_proof}{proof}'.encode()
         guess_hash = hashlib.sha256(guess).hexdigest()
         return guess_hash[:4] == "0000"

     #----------------------------------------------------------------------------------------------------#

     # Main()
     if __name__ == '__main__':
     	print('UI Implementation Pending...')


     #----------UserInterface----------#


