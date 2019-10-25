"""
EVINGTONE NGOA MWAILONGO

HOW TO RUN
1. Open Three Terminals. 
2. One Terminal run ``` python kdc.py```
3. One Terminal run ``` python alice.py```
4. Second Terminal run   ``` python bob.py```
"""
# first of all import the socket library 
import socket			 
import time		
import random	
import utils

ALICE_INITIAL_SECRET_KEY = "This-is-Alice-secret-1624259"
BOB_INITIAL_SECRET_KEY = "This-is-Bob-secret-1339185"
KDC_INITIAL_SECRET_KEY = "This-is-Alice-secret-1339185"

# reserve a PORT on your computer in our 
# case it is 12345 but it can be anything 
PORT = 12345	
ALICE_PORT = 12346
BOB_PORT = 12347	
HOST = 'localhost'		
server_address = (HOST, BOB_PORT)	
SLEEPING_TIME = 3

def initSocketCommunication(PORT, HOST, server_address):
    listKeys = [1,2]

    # next create a socket object 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	

    # Register Bob To this Port
    s.bind(server_address)		 

    print(" Socket bind to %s" %(BOB_PORT)) 
    time.sleep(SLEEPING_TIME)
    receiveMsg(s, listKeys)	

# Function to Listen and Receive
# Messages sent from Client
def receiveMsg(s, listKeys):
    # put the socket into listening mode 
    s.listen(5)	 
    print(" Socket is listening...")
    # brand()

    time.sleep(SLEEPING_TIME)

    # a forever loop until we interrupt it or 
    # an error occurs 
    while True: 

        # Establish connection with client. 
        conn, addr = s.accept()	 
        print('\n Got connection from', addr )
        time.sleep(SLEEPING_TIME)

        while True:
            data = conn.recv(1024)
            print('\n Received From Client: {!r}'.format(data))
            time.sleep(SLEEPING_TIME)

            # decode Message
            decodedMsg = data.decode()

            if data:
                # Bob Receiving Session Key from KDC
                if(decodedMsg.find('_') != -1):
                    # exctract Key from string
                    bobInitKey = utils.extractKey(BOB_INITIAL_SECRET_KEY)

                    print(f"\n bobInitKey => {bobInitKey}\n")

                    # Decrypts Session Key Message Cipher from KDC
                    plaintext = utils.decryptionProcess(decodedMsg, bobInitKey, '_')
                    time.sleep(SLEEPING_TIME)

                    print(f"\n Session Key => {plaintext}\n")
                else:
                    sessionKey = utils.extractKey(plaintext)

                    print(f"\n Message Received From Alice => {decodedMsg}\n")

                    print(f"\n Extracted Session Key => {sessionKey}\n")

                    time.sleep(SLEEPING_TIME)
                    # Decrypts Session Key Message Cipher from KDC
                    plaintext = utils.decryptionProcess(decodedMsg, sessionKey, '-')

                    print(f"\n Message From Alice => {plaintext}\n")

                    time.sleep(SLEEPING_TIME)

                    break


            else:
                print(' No data from client with Address : ', addr)

                break



        # Close the connection with the client 
    conn.close() 



def main():
    initSocketCommunication(PORT, HOST, server_address)

    print(f"Alice -> {ALICE_INITIAL_SECRET_KEY}\n")
    print(f"Bob -> {BOB_INITIAL_SECRET_KEY}\n")



if __name__ == '__main__':
    main()

