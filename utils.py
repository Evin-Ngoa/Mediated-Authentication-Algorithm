# Import socket module 
import socket  

# Extract Secret Key from
# Text Key 
# expecting format message-234324 args(str)
# returns 234324 ( int )
def extractKey(secretKeyText):
    splitText = secretKeyText.split('-')

    # convert the lastvalue into integer
    secretKeyValue = int(splitText[-1])

    return secretKeyValue

# Encryption Logic with Key
# expects Plaintext and encryption Key (str, int)
# return string
def encryptionProcessData(word, encryptionKey, symbol):
    encValList = []
    # Convert the word into list chars
    wordList = list(word)

    print("\nEncryption Key => ", encryptionKey)

    for char in wordList:
        unicodeChar = ord(char)
        # Hashing the word with the Key
        encValList.append( unicodeChar * encryptionKey)

    # Convert each value in list into string
    encValList = list(map(str, encValList))

    encValList = symbol.join(str(intVal) for intVal in encValList)
    # encValList = "_".join(str(intVal) for intVal in encValList)
    print(f"encValList Cipher => {encValList}\n")

    return encValList

# Decrypting the Message from Client Using the 
# args (str, int)
# return string
def decryptionProcess(cipherTxt, decryptionKey, symbol):
    decValList = []

    # Split Cpher
    # splitText = cipherTxt.split('_')
    splitText = cipherTxt.split(symbol)

    # Converting all strings in th list to integers.
    splitText = list(map(int, splitText))

    print("\nDecryption Key => ", decryptionKey)

    for char in splitText:
        # Compute Original Unicode
        getUnicode = int(char / decryptionKey)
        # Convert Each Char from Unicode
        decryptedChar = chr(getUnicode)
        decValList.append( decryptedChar )

    plaintext = "".join(decValList)

    return plaintext

# def sendData(client_socket, serverLocahost, msg, TO_PORT):
def sendData(serverLocahost, msg, TO_PORT):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((serverLocahost, TO_PORT))
    print(f"Sending DATA ---------")
    while 1:
        # data = msg
        data =  bytes(msg, 'utf-8')

        client_socket.sendall(data)
        client_socket.close()
        break;


def main():

    print(f"Testing Utils ...\n")

    keyText = "i-am-selling-this-code-for-1181351"

    key = extractKey(keyText)

    print(f"Key => {key}\n")

    msg= "i need to talk to Bob"

    cipherTxt = encryptionProcessData(msg, key)

    print(f"cipherTxt => {cipherTxt}\n")

    plaintext = decryptionProcess(cipherTxt, key)

    print(f"plaintext => {plaintext}\n")


if __name__ == '__main__':
    main()