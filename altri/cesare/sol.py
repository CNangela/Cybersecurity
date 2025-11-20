import base64
import string

ALPHABET = list(string.printable)  
LEN = len(ALPHABET)

def rotate(msg,n):
    rot13_enc = ''
    for c in msg:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i - n)%LEN]
    return rot13_enc


def decodeb64(msg):
    return base64.b64decode(msg).decode('ascii', errors="ignore")

with open("encrypted_flag.txt","r") as file:
    msg = file.read()
    file.close()
print(msg)
print(decodeb64(rotate(msg,13)))