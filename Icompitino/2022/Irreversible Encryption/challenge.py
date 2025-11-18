#!/usr/bin/env python3

import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100
#string.printable contiene tutti i caratteri considerati stampabili, non sono lettere
# ma anche (){}-+:* ecc
LEN = len(ALPHABET)

FLAG = "??????????????????????????????????????????????"

# b64 encoding is safe and my flag secure
def base64encode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64encode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

# same for b32
def base32encode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32encode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

# I think I'm forgetting something important to remove here (la chiave?)
def XORencode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    # ALLORA, CHE FA ZIP INTANTO??? accoppia elementi iterabili come liste, esempio:
    # a = [1,2,3] b = ['a', 'b', 'c']
    # zip(a,b) ottieni [(1,'a'),(2,'b'),(3,'c')]

    #bene, ora che lo sappiamo, possiamo continuare
    #zip sta accoppiando ogni carattere del messaggio e della chiave, e la chiave modificata è
    # grande quanto il messaggio
    # l'operatore ^ fa lo xor, (e se sono caratteri tipo 'a' 'b' allora lo fa del loro binario in ascii)
    # bene, allora, c'è uno xor tra il messaggio e la chiave, ok e poi questo è trasformato in carattere, quindi
    # prendo il valore del carattere nell'ascii che ho ottenuto dallo xor tra a e b 
    # --> riassunto ottengo lo xor di a e b in carattere ascii

    # la forma ''.join ecc è solo per non fare un ciclo, comunque come funziona lo abbiamo capito
    return xored

# Easy-to-use function, that looks useful
def ROTencode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c) # ottengo l'indice dove si trova c
        rot13_enc += ALPHABET[(i+pos)%LEN] #sto ruotando in base alla posizione che gli sto, sembra cesare
    return rot13_enc

# a useless method that could be replaced by a single line of code
# why not?
def ascii_to_hex(message):
    encoded = binascii.hexlify(message).decode()
    #converte una sequenza di bytes in una rappresentazione esadecimale binascii.hexlify(message)
    #.decode() converte l'esadecimale ottenuto in un utf-8 di default
    return encoded

# do it 15 times plz
encrypted = "Encode as if there's no tomorrow: " + FLAG
for _ in range(15):
    # encode the FLAG in the 4 different ways, always the same order
    b64_encrypted = base64encode(encrypted)
    rot13_encrypted = ROTencode(b64_encrypted, 13)
    b32_encrypted = base32encode(rot13_encrypted)
    encrypted = ROTencode(b32_encrypted, 3)

#  I was told that XOR is a secure operation
xor_encrypted = XORencode(encrypted).encode('ascii')

# hopefully also the hex encoding will strengthen the encryption operation
hex_encrypted = ascii_to_hex(xor_encrypted)

# save the result for later use
# none will decrypt it anyway
with open("encrypted_flag.txt", "w") as f:
    f.write(hex_encrypted)
    f.close()

