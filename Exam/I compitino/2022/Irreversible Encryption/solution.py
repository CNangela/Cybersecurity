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
def base64decode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64decode(message_bytes) #cambio qua con decode
    b64_message = b64_bytes.decode('ascii')
    return b64_message

# same for b32
def base32decode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32decode(message_bytes) #cambio qua con decode
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
    # message_bytes = message.encode('ascii')
    encoded = binascii.hexlify(message)
    return encoded




# save the result for later use
# none will decrypt it anyway
with open("encrypted_flag.txt", "r") as f:
    text = f.read()
    f.close()

#facciamo i passaggi al contrario, prima riportiamolo in ascii
decoded = binascii.unhexlify(text)
decoded = decoded.decode('ascii')

#ora tocca allo xor, so che A XOR B = C  ⇒  C XOR B = A, quindi
decoded = XORencode(decoded)


#e qui faccio come prima ma al contrario e con il negativo sugli indici
# do it 15 times plz
for _ in range(15):
    # encode the FLAG in the 4 different ways, always the same order
    decoded = ROTencode(decoded, -3)
    decoded = base32decode(decoded)
    decoded = ROTencode(decoded, -13)
    decoded = base64decode(decoded)

print(f'soluzione (speriamo): {decoded}')

#flag: spritz{But_wa1t_R3vers1ble_OP3rations_are_B4D}


