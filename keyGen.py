"""
EVINGTONE NGOA MWAILONGO

"""
import random
import time	

SLEEPING_TIME = 3

# Check if the value Pass is a prime number
def isPrime(val):
    if (val==1):
        return False
    elif (val==2):
        return True
    else:
        for x in range(2,val):
            if(val % x==0):
                return False
        return True 

# Geerate Random Prime Numbers over 100
def getPrime():
    Min = 100
    Max = 200
    # Will stop when isprime returns true 
    # then exits when return primeVal 
    # has been activated
    while(1):
        primeVal = random.randint(Min,Max)
        # print("primeVal ",primeVal)
        if isPrime(primeVal):
            return primeVal

def definePQ():
    p = getPrime()
    q = getPrime()
    # print("Step 1 : p ",p , "q ",q)
    PQList = [p,q]
    
    return PQList

def phiN(PQList):
    p = PQList[0]
    q = PQList[1]

    phiOfN = (p - 1) * (q - 1)
    # print(" phiOfN ========> ", phiOfN)

    return phiOfN

# Get Factors of product
def getFactors(product):
    factorsList = []
    # print("The factors of ",product," are:")

    for i in range(2, product + 1):
        if product % i == 0:
            factorsList.append(i)

    return factorsList

# Function to generate range of 
# numbers lesser than [0N]
def getLessCoprimeRange(phiNVal):

    possibleCoprimesList = []

    for i in range(1,phiNVal): 
        # add the range into a list
        possibleCoprimesList.append(i)

    return possibleCoprimesList

def getEFromMemberList(getPossibleCoprimesList , outputFactors):
    # print(f"Divisor:{getPossibleCoprimesList}")
    # print(f"Dividend:{outputFactors}")

    for divisor in range(1, len(getPossibleCoprimesList) + 1):
        for dividend in outputFactors:  
            # print("member mod factor ", divisor, " and ",  dividend)      
            if(divisor%dividend) == 0:
                getPossibleCoprimesList.remove(divisor)
                # If has removed the value
                break

    # print("Final **** ", getPossibleCoprimesList)

    return getPossibleCoprimesList
        
def findE(phiNVal, PQList):
    getPossibleCoprimesList = getLessCoprimeRange(phiNVal)

    # print("Possible Value in List => ", getPossibleCoprimesList)
    getFactorsList = getFactors(phiNVal)

    # print("P , Q and Factors of phinN => ", PQList, getFactorsList)
    outputFactors = list(PQList) 

    # Copies list from outputFactors to getFactorsList
    outputFactors.extend(y for y in getFactorsList if y not in outputFactors) 
    # print("Combined factors => ", outputFactors)

    eValuesList = getEFromMemberList(getPossibleCoprimesList , outputFactors)

    # Delete 1 from the list which will always be on the 
    del eValuesList[0]

    # print(f"The values of e {eValuesList}")

    return eValuesList

def findD(eValue, phiNVal, nValue):
    
    for val in range(1, 100000):
        # if d not equal to n and e not equal to e
        if(((val * eValue) % phiNVal) ==1 and eValue != val and nValue != val):
            d = val
            # if satisfies the equation break
            break
    return d

def promptMessage():
    word = str(input("\nEnter A Word To Be Ciphered Through RSA: "))
    if not word.strip():
        print("\nERROR : Invalid Word, Enter A Word")
        word = promptWord()
    return word

def encryptRSA(msg, eVal, nVal):

    unicodeChar = [pow(ord(char),eVal,nVal) for char in msg]

    return unicodeChar

def decryptRSA(ciphertext, dVal, nVal):

    decoded = [chr(pow(char, dVal, nVal)) for char in ciphertext]

    plaintext = "".join(decoded)

    return plaintext



def getPublicPrivate():

    PQList = definePQ()
    nValue = PQList[0] * PQList[1]

    # print("Step 1 : P and Q in List ", PQList[0], PQList[1])
    # print("Step 1 : N VAlue ", nValue)

    phiNVal = phiN(PQList)
    # print("Step 2 : PhiN [0N] =====> ", phiNVal)

    # print("Step 3 : Finding e")
    eValues = findE(phiNVal, PQList)
    eValue = eValues[0]
    # print("Step 3 : E =====> ", eValue)

    dValue = findD(eValue, phiNVal, nValue)
    # print("Step 4 : D =====> ", dValue)
    # print(f"\nGenerating Keys ... \n")
    # time.sleep(4)
    
    # print(f"(e,N) (d,N) =====> Pubclic Key = ({eValue}, {nValue}) || Public Key= ({dValue}, {nValue})")

    privatePublicKey = [eValue , nValue, dValue, nValue]

    return privatePublicKey


def main():
    keys = getPublicPrivate()

    print(f"Generating Keys ...\n")

    time.sleep(SLEEPING_TIME)

    print(f"\nGenerated Keys ====> {keys}")

if __name__ == '__main__':
    main()