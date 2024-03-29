
 > NAME        : EVINGTONE NGOA
 > TITLE       : Mediated Authentication
 > LANGUAGE    : PYTHON 3
 
 # Mediated Authentication ALGORITHM
A very basic implementation of Mediated Authentication written in Python
### How It Works
---------------------------------------------------------------------------------------- 
1. Alice sends encrypted msg `I need to communicate with BOB, kindly send session key` to KDC encrypted with private key, K(A).
2. KDC Decrypts the message using the same secret key K(A) and confirms that it is from Alice.
3. KDC Generates the session key for A and B, K(AB).
5. KDC encrypts the generated session key using the shared key with Alice, K(A), and sends to Alice
6. KDC encrypts the generated session key using the shared key with Bob, K(B), and sends to Bob 
7. Alice decrypts using shared key K(A) cipher from KDC and gets the session key.
8. Bob decrypts using shared key K(B) the cipher from KDC and gets the session key.
9. Alice encrypts 'hello Bob' Message with the session key and sends to BOB
10. Bob decrypts the message using the session key.

DONE
--------------------------------------------------------------------------------------- 
# How To Run
1. Clone The Project
2. Navigate Into The Folder
3. Open THREE Terminals
4. One Terminal run ``` python kdc.py```
5. Second Terminal run   ``` python bob.py```
6. Third Terminal run   ``` python alice.py```

## Enjoy!!



[Check out my Portfolio](http://evin.me.ke/ "Evin's portfolio")
![alt text](http://evin.me.ke/wp-content/uploads/2016/07/evin-100X50.png "Check Out My portfolio")