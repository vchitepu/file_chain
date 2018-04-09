# Cryptek Security LLC.
# FileChain Secure Data Storage
# Created By: Vinay Chitepu
# Written in Python 3.6

# IMPLEMENTATION: 
# Using a blockchain to store files. Files are stored using thier basis hex values so that they can be 
# later reconstructed to from the hex values using xxd bash when they are needed. Every change(new save) will be treated 
# as a seperate block in the chain. This is a Beta for the FileChain system. 

# DESIGN: 
# This software essentially uses the blockchain ADT to securely store files and data. The every change is added in since 
# there is a different hex value hence every version of the previously saves file can be accessed. Since the blockchain is also 
# immutable no changes can be made to it and it is difficult to access files on it without local permissions. 

# TO-DO:
# Create a database of chains for useres
# Integrate a cloud system to store every clients individual chain. Once the program is started a new chain is created locally and 
# copied over from the cloud. After the program is quit out of the new changes made to the chain are pushed back into the cloud.


#----------------------------------------------------MODULES-----------------------------------------------------#

import hashlib
import json
import os
import os.path
import tkinter as tk
from time import time
from uuid import uuid4
from tkinter import filedialog
from datetime import datetime

#-----------------------------------------------------CLASS------------------------------------------------------#

class Filechain:

	 # Initialize the chain (happen during startup)
     def __init__(self):
         self.timestamps = []
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
         self.timestamps.append(block['timestamp'])


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
             'file_path': pathcorrector_os(file_path),
             'data': data
         }
         if(self.file['data'] != ''):
             self.files_in_chain.append(self.file['file_path'])
         return self.last_block['index'] + 1

     #----------------------------------------------------------------------------------------------------#

     # Returns the last block of the chain
     @property
     def last_block(self):
        return self.chain[-1]

     #----------------------------------------------------------------------------------------------------#

     # Opens a file using the hexdump
     def open_file(self, index, file_name):
        # :param index: <int> Index of block on the chain where the hexdump in located
        # :param file_name: <str> The name of the file that we are going to open

        data = self.chain[index]['file']['data']

        textfile = open('hexfiletemp.txt', 'w')
        textfile.write(data)
        textfile.close()

        os.system('xxd -r hexfiletemp.txt > temporary')
        os.system('open temp') 
        os.system('rm hexfiletemp.txt')


     #----------------------------------------------------------------------------------------------------#

   	 # Creates a SHA-256 hash of a Block
     @staticmethod
     def hash(block):
         # :param block: <dict> Block
         # :return: <str> hash for the block
        
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
    print(' __________     ___     ___             __________     __________     ___        ___              ___              ___       ___       ___  ')
    print('|          |   |   |   |   |           |          |   |          |   |   |      |   |            /   \            |   |     |    \    |   | ')
    print('|    ______|   |   |   |   |           |    ______|   |    ______|   |   |      |   |           /     \           |   |     |     \   |   | ')
    print('|   |          |   |   |   |           |   |          |   |          |   |      |   |          /  __   \          |   |     |      \  |   | ')
    print('|   |______    |   |   |   |           |   |______    |   |          |   |______|   |         /  /  \   \         |   |     |       \ |   | ')
    print('|          |   |   |   |   |           |          |   |   |          |              |        /  /____\   \        |   |     |   |\   \|   | ')
    print('|    ______|   |   |   |   |           |    ______|   |   |          |    ______    |       /             \       |   |     |   | \       | ')
    print('|   |          |   |   |   |           |   |          |   |          |   |      |   |      /   _________   \      |   |     |   |  \      | ')
    print('|   |          |   |   |   |_______    |   |______    |   |______    |   |      |   |     /   /         \   \     |   |     |   |   \     | ')
    print('|   |          |   |   |           |   |          |   |          |   |   |      |   |    /   /           \   \    |   |     |   |    \    | ')
    print('|___|          |___|   |___________|   |__________|   |__________|   |___|      |___|   /___/             \___\   |___|     |___|     \___| ')
    print('Secure File Storage')
    print('Cryptek Security')
    print('')
    print('NOTE: Increase the size of terminal if image appears distored')
    print('')

#---------------------------------------------------------------------------------------------------IMPLEMETATION---------------------------------------------------------------------------------------------------#

# Formats timestamp into datatime 
def timestamp2datetime(timestamp):
    # :param timeestamp: <str> timstamp of each block
    # :return: Formatted timestamp

    return datetime.fromtimestamp(timestamp).isoformat()


# Opens local file browser and gets file path
def getFilePath():
    # :return: filepath for selected file
   root = tk.Tk()
   root.withdraw()
   file_path = filedialog.askopenfilename()
   return file_path

def pathcorrector_xxd(file_path):
    arr = []
    for x in file_path:
        if(x == ' '):
            arr.append('\\')
        arr.append(x)
    corrected = ''.join(arr)
    return corrected

def pathcorrector_os(file_path):
    count = 0
    for x in file_path:
        if(x == "\\"):
            count+=1
    
    file_path = file_path.replace('\\', '', count)
    return file_path

# Main()
def main(): # User Interface

#-----------------------------------------------------------------------------------------------------MAIN_MENU-----------------------------------------------------------------------------------------------------#
    printOpening()

    print('Welcome to your File System')
    print('')
    f = Filechain() # Creates a new filechain

    run = True
    while run:
        print('--------------------------------------------------------------------------------------------------------')
        print('')
        print("Menu: ")
        print('')
        print("1. Add File")
        print("2. Show/Open files")
        print("Q. Quit")
        print('')
        option = input('Enter choice here: ')

#-----------------------------------------------------------------------------------------------------ADDFILE-------------------------------------------------------------------------------------------------------#

        if(option == '1'):
            runOption1 = True
            while runOption1:
                print('')
                print('--------------------------------------------------------------------------------------------------------')
                print('')
                print('ADD FILE')
                print('')
                print('')
                print("Options:")
                print('')
                print("- 1. Open File Browser")
                print("- Q. Back to main menu")
                print('')
                print('           OR')
                print('')
                print("- RECOMMENDED: Drag and drop the file into the terminal or type the filepath correctly below")
                print('')
                option1 = input('Enter choice or filepath here and press enter: ')
                if(option1 == '1'):
                    file_path = getFilePath()
                    if(file_path == ''):
                        print('')
                        print('Add cancelled')
                        print('')    
                    else:
                        print('')
                        print('--------------------------------------------------------------------------------------------------------')
                        print('')
                        print('ADDED: ' + file_path + ' added successfully')
                        f.new_file(pathcorrector_xxd(file_path))
                        proof = f.proof_of_work(f.last_block['proof'])
                        previous_hash = f.hash(f.last_block)
                        f.new_block(proof, previous_hash)

                elif(option1 == 'q' or option1 == 'Q'):
                    runOption1 = False
                else:
                    option1 = option1[:len(option1)-1]
                    if(os.path.exists(pathcorrector_os(option1))):
                        file_path = option1
                        print('')
                        print('--------------------------------------------------------------------------------------------------------')
                        print('')
                        print('ADDED: ' + pathcorrector_os(file_path) + ' added successfully')
                        f.new_file(file_path)
                        proof = f.proof_of_work(f.last_block['proof'])
                        previous_hash = f.hash(f.last_block)
                        f.new_block(proof, previous_hash)
                    else:
                        print('')
                        print("File does not exist")


#-----------------------------------------------------------------------------------------------------OPENFILE-------------------------------------------------------------------------------------------------------#

        elif(option == '2'):
            print('--------------------------------------------------------------------------------------------------------')
            print('')
            print('Chain: ')
            print('')
            if(f.files_in_chain == []):
                print('     -none-')
            count = 1
            for x in f.chain:
                if(x == f.chain[0]):
                    continue
                else:
                    print(str(count) + '. Name: ' + str(x['file']['file_path']) + '      Date/Time of Save: ' + str(timestamp2datetime(x['timestamp'])))
                    count+=1

            run2 = True
            while run2:
                print('')
                
                print('')
                print('--------------------------------------------------------------------------------------------------------')
                print('')
                print('Open Files')
                print('')
                print('NOTE: Once the file is opened you must save it manually if you wish to keep it')
                print('')
                option3 = input("Choose file number to open or type 'q' to go back to the main menu: ")
                if(option3 == 'q' or option3 == 'Q'):
                    run2 = False
                    os.system('rm temp')

                else:
                    try:
                        option3 = int(option3)
                        if(int(option3) < len(f.chain)):
                            block = f.chain[option3]
                            file_name = block['file']['file_path']
                            f.open_file(option3, file_name)
                        else:
                            print('')
                            print('ENTER A VALID OPTION')

                    except ValueError:
                        print('')
                        print("ENTER A VALID OPTION")


#-------------------------------------------------------------------------------------------------------EXIT--------------------------------------------------------------------------------------------------------#


        elif(option == 'q' or option == 'Q' ):
            run = False
            print('')
            print('Thank You!')
            print('Quitting...')
        else:
            print("")
            print('ENTER A VALID OPTION')


        print('')
        print('')
    
if __name__ == '__main__': 
    main()
    os.system('clear')
    
    print('Thank You!')
    print('Quitting...')
    print('')
    






             	
    
  


     


