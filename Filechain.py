# Cryptek Security
# FileChain Secure Data Storage
# Developed By: Vinay Chitepu

# IMPLEMENTATION: Using a blockchain to store files. Files are stored using thier basis hex values so that they can be 
# later reconstructed to from the hex values using xxd bash when they are needed. Every change(new save) will be treated 
# as a seperate block in the chain.


# Imported Modules
import hashlib
import json
import os
import tkinter as tk
from time import time
from uuid import uuid4
from tkinter import filedialog
import warnings
warnings.filterwarnings("ignore")


#-----------------------------------------------------CLASS------------------------------------------------------#


class Filechain:

	#Initialize the chain
     def __init__(self):
         self.files_in_chain = []
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
         self.files_in_chain.append(file_path)
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




#---------------------------------------------------END-CLASS----------------------------------------------------#

#Opening in terminal
def printOpening():

    print('')
    print('')
    print('  __________     ___     ___             __________     __________     ___        ___              ___              ___       ___       ___     ')
    print(' |          |   |   |   |   |           |          |   |          |   |   |      |   |            /   \            |   |     |    \    |   |    ')
    print(' |    ______|   |   |   |   |           |    ______|   |    ______|   |   |      |   |           /     \           |   |     |     \   |   |    ')
    print(' |   |          |   |   |   |           |   |          |   |          |   |      |   |          /  __   \          |   |     |      \  |   |    ')
    print(' |   |______    |   |   |   |           |   |______    |   |          |   |______|   |         /  /  \   \         |   |     |       \ |   |    ')
    print(' |          |   |   |   |   |           |          |   |   |          |              |        /  /____\   \        |   |     |   |\   \|   |    ')
    print(' |    ______|   |   |   |   |           |    ______|   |   |          |    ______    |       /             \       |   |     |   | \       |    ')
    print(' |   |          |   |   |   |           |   |          |   |          |   |      |   |      /   _________   \      |   |     |   |  \      |    ')
    print(' |   |          |   |   |   |_______    |   |______    |   |______    |   |      |   |     /   /         \   \     |   |     |   |   \     |    ')
    print(' |   |          |   |   |           |   |          |   |          |   |   |      |   |    /   /           \   \    |   |     |   |    \    |    ')
    print(' |___|          |___|   |___________|   |__________|   |__________|   |___|      |___|   /___/             \___\   |___|     |___|     \___|    ')
    print(' The most secure file storage system')
    print(' By: Crptek Security')
    print('')
    print('')

#-------------------------------------------------IMPLEMETATION--------------------------------------------------#




# Opens local file browser and gets file path
def getFilePath():
   root = tk.Tk()
   root.withdraw()
   file_path = filedialog.askopenfilename()
   return file_path
    

# Main()
def main():
    #---------------UserInterface--------------#
    printOpening()

    print('Welcome to your File System')
    print('')
    f = Filechain() # Creates a new filechain

    run = True
    while run:
        print("Menu: ")
        print('')
        print("1. Add File")
        print("2. Show my files")
        print("3. Quit")
        option = input('Enter choice here: ')



        if(option == '1'):
            print('Please select file to add...')

            #------------LocalFileBrowserOpen-----------#

            file_path = getFilePath()
            if(file_path == ''):
                print('')
                print('File not added...')
                print('')
                continue
            f.new_file(file_path)
            proof = f.proof_of_work(f.last_block['proof'])
            previous_hash = f.hash(f.last_block)
            f.new_block(proof, previous_hash)
        elif(option == '2'):
            print('')
            print('Chain: ')
            print('')
            if(f.files_in_chain == []):
                print('     -none-')
            for x in f.files_in_chain:
                print('     ' + x)
        elif(option == '3'):
            run = False
            print('')
            print('Thank You!')
            print('Quitting...')
        else:
            print("")
            print('ENTER A VALID OPTION')


        print('')
 

if __name__ == '__main__': main()

    






             	
    
  


     


