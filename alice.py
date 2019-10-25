"""
EVINGTONE NGOA MWAILONGO

HOW TO RUN
1. Open Three Terminals. 
2. One Terminal run ``` python kdc.py```
3. One Terminal run ``` python alice.py```
4. Second Terminal run   ``` python bob.py```
"""

# Import socket module 
import socket                
import time  
import keyGen    
import random
import utils

# Define the port on which you want to connect 
PORT = 12345	
BOB_PORT = 12347	
HOST = 'localhost'		
server_address = (HOST, PORT)	
SLEEPING_TIME = 3
MESSAGE = 'Alice need to communicate with BOB, kindly send session key'  
TO_BOB_MESSAGE = "Hello Bob"
KDC_INITIAL_SECRET_KEY = "This-is-Alice-secret-1624259"

# initiate Port Connection
def iniPortCommunication():
    # Create a socket object 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    # Register KDC To this Port
    # sock.bind(server_address)  

    # connect to the server on local computer 
    sock.connect(server_address) 

    # exctract Key from string
    key = utils.extractKey(KDC_INITIAL_SECRET_KEY)

    print(f"Key => {key}\n")

    # Sending Permission Message
    cipher = utils.encryptionProcessData(MESSAGE, key, "_")

    cipherSecretbyte = bytes(cipher, 'utf-8')
    
    print(f"Sending \'Alice needs to communicate with BOB, kindly send session key\' to Server ...")
    time.sleep(SLEEPING_TIME)

    # Send cipher
    initMsgSender(sock, cipherSecretbyte)

    # Get Listen from KDC
    while True:
        # put the socket into listening mode 
        # sock.listen(5)	
        print(f"Listening...")

        # Receiving Server Message
        # receive data from the server 
        data = sock.recv(1024)

        #decode Message
        decodedMsg = data.decode()

        print(f"\n Message From Server => {decodedMsg}")

        # Decrypts Session Key Message Cipher from KDC
        plaintext = utils.decryptionProcess(decodedMsg, key, '_')

        print(f"\n Session Key => {plaintext}\n")

        sessionKey = utils.extractKey(plaintext)

        print(f"\n Extracted Session Key => {sessionKey}\n")

        time.sleep(SLEEPING_TIME * 3)

        break

    # close the connection 
    sock.close() 

    # From Alice Sending to BOB
    print(f"Preparing my message...")

    # Sending Permission Message
    cipherMsgBob = utils.encryptionProcessData(TO_BOB_MESSAGE, sessionKey, "-")

    time.sleep(SLEEPING_TIME)

    print(f"Sending \' {TO_BOB_MESSAGE} \' to Bob...")

    utils.sendData(HOST, cipherMsgBob, BOB_PORT)
    time.sleep(SLEEPING_TIME)

    print('\n Done Sending Hello Message to Bob... ')
    time.sleep(SLEEPING_TIME)



# Ensures Message Sent
def initMsgSender(sock, message):
    sock.sendall(message)


def main():
    print(f"KDC -> {KDC_INITIAL_SECRET_KEY}\n")
    iniPortCommunication()





if __name__ == '__main__':
    main()

