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

# reserve a PORT on your computer in our 
# case it is 12345 but it can be anything 
PORT = 12345	
ALICE_PORT = 12346
BOB_PORT = 12347	
HOST = 'localhost'		
server_address = (HOST, PORT)	
bob_server_address = (HOST, BOB_PORT)	
SLEEPING_TIME = 3

def initSocketCommunication(PORT, HOST, server_address):
    listKeys = [1,2]

    # next create a socket object 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	

    # Register KDC To this Port
    s.bind(server_address)		 

    print(" Socket bind to %s" %(PORT)) 
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
                # Alice initial encryption
                if(decodedMsg.find('_') != -1):
                    # Get Keys
                    aliceKey = utils.extractKey(ALICE_INITIAL_SECRET_KEY)
                    bobkey = utils.extractKey(BOB_INITIAL_SECRET_KEY)
                    
                    print(f"\n Message from Alice => {decodedMsg}")

                    # Decrypts Message
                    plaintext = utils.decryptionProcess(decodedMsg, aliceKey, '_')

                    print(f"\n plaintext => {plaintext}\n")

                    # Alice Confirmation 
                    if(plaintext.find('Alice') != -1):
                        print(f"\n Alice Confirmed! ")
                        # GENERATE SESSION KEYS
                        sessionKey = genAuthKey()

                        # Sending Permission Message to Alice
                        aliceCipher = utils.encryptionProcessData(sessionKey, aliceKey, "_")
                        bytMsg = bytes(aliceCipher, 'utf-8')
                        # send a thank you message to the Alice. 
                        # conn.sendall(bytMsg) 
                        print('\n Sending Session Key to Alice... ')
                        time.sleep(SLEEPING_TIME)
                        conn.sendto(bytMsg, server_address) 
                        print('\n Done Sending Session Key to Alice... ')
                        time.sleep(SLEEPING_TIME)
                        conn.close() 

                        # Sending Permission Message to Bob
                        bobCipher = utils.encryptionProcessData(sessionKey, bobkey, "_")
                        # bytMsgAlice = bytes(bobCipher, 'utf-8')
                        print('\n Sending Session Key to Bob... ')
                        time.sleep(SLEEPING_TIME)
                        utils.sendData(HOST, bobCipher, BOB_PORT)
                        time.sleep(SLEEPING_TIME)
                        print('\n Done Sending Session Key to Bob... ')
                        break
                       

            else:
                print(' No data from client with Address : ', addr)

                break



        # Close the connection with the client 
    # conn.close() 
    
# Generate Authentication Certificates
def genAuthKey():
    print(f"\n Generating Authentication Certificates ... \n")

    time.sleep(SLEEPING_TIME)

    prefixKey = "session-key-Alice-Bob-"

    generatedSecretKey = secretKeyGen(prefixKey)

    return generatedSecretKey

# Generate Secret Key
# encrypt with RSA 
# send to server to get the secret key
def secretKeyGen(prefixKey):
    Min = 1000000
    Max = 2000000
    print(f"\nGenerating Secret Session Key...\n")

    time.sleep(SLEEPING_TIME)
    secretVal = random.randint(Min,Max)
    # secretK = "i-am-selling-this-code-for-" + str(secretVal)
    secretK = prefixKey + str(secretVal)

    print(f"\nSecret Key => {secretK}\n")

    return secretK



def main():
    initSocketCommunication(PORT, HOST, server_address)

    print(f"Alice -> {ALICE_INITIAL_SECRET_KEY}\n")
    print(f"Bob -> {BOB_INITIAL_SECRET_KEY}\n")



if __name__ == '__main__':
    main()

