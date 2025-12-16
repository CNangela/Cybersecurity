#!/usr/bin/env python3

# encryption method
def encryption(plain_text, key):
    encrypted_text = ""
    # sta creando una chiave della lunghezza del testo
    key_extended = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]

    # ciclo che si ripete per tutto il testo passato
    for i in range(len(plain_text)):
        char_plain = plain_text[i]
        char_key = key_extended[i]

        # suppongo serva per avere solo lettere minuscole, perché queste partono da 97
        offset = 97

        if char_plain.isalpha(): # controllo se è una lettera
            # here is the most important part
            encrypted_char = chr((ord(char_plain) + ord(char_key) - 2 * offset) % 26 + offset)

            #cosa fa:
            # prende il valore ascii del char_plain e lo somma al valore ascii della chiave, sottrae poi 97*2, 
            # il valore che ottiene è ad esempio 97 ('a') + 122 ('z') - 97*2 = 25
            # a questo fa il mod di 26 (numero di lettere dell'alfabeto) e ottiene 1, a questo somma l'offset 97, 
            # ottieni 98 --> 'b'
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char_plain
            # se non è una lettera lo lascia com'è

    return encrypted_text

# key for the encryption
k = "tellmewhy" #suppongo sia la chiave da allungare quanto il testo con l'operazione sopra

# this is my message
flag = 'spritz{i-want-it-that-way}'
        
c = encryption(flag, k)
print("Encrypted text:", c)

# OUTPUT: ltctfd{p-peye-mp-raee-ieu}