#!/usr/bin/env python3

#sull'osservazione del codice posto

# decryption method
def decryption(message, key):
    decrypted_text = ""
    key_extended = (key * (len(message) // len(key))) + key[:len(message) % len(key)]

    for i in range(len(message)):
        char_plain = message[i]
        char_key = key_extended[i]

        offset = 97

        if char_plain.isalpha():
            # here is the most important part
            decrypted_char = chr((ord(char_plain) - ord(char_key)) % 26 + offset)
            # modifiche: intanto anziché sommare la chiave, la devo togliere e poi
            # l'offset*2 mi servire perché ottenevo un numero alto, tipo nell'esempio di prima 219, quindi devo 
            # togliere la parte in eccesso, ovvero 194, qui invece sto sottraendo, quindi ad esempio faccio
            # 97 ('a') - 122 ('z') = -25 e con %26 ottengo 1 + 97 = 'b'
            #se invece lo tenevo avevo 97 ('a') - 122 ('z') = -219 e con %26 11 + 97 = 'l'
            # considerando l'esempio che ho fatto nel file precedente, doveva venire 'b' e non 'l'
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char_plain

    return decrypted_text

# key for the encryption
k = "tellmewhy"

# this is my message
message = 'ltctfd{p-peye-mp-raee-ieu}'
        
c = decryption(message, k)
print("decrypted text:", c)

#flag spritz{i-want-it-that-way}

# e se lo sostituisco alla flag precedente, ottengo ltctfd{p-peye-mp-raee-ieu}
# cioè quello che c'era scritto come commento di output