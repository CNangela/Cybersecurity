import base64

def replace_chars(text, dict):
    replaced_text = ""
    
    # per ogni lettera contenuta in text (non fare text[x], non si tratta di indici, 
    # ma proprio del contenuto in posizione x (si python semplifica troppo che schifo))
    for c in text: 
        #get(c,c) prendi dal dizionario il valore associato alla chiave c, se non esiste, restituisci c stesso
        #(e io questo come facevo a saperlo???)
        replaced_text += dict.get(c, c)

    return replaced_text


#legge il file
with open("ciphertext.txt", "r") as f:
    ZO_text = f.read()
    f.close()

ZO_dict = {"Z":"0", "O":"1"} # mappa 0 quando compare Z ecc
text = replace_chars(ZO_text, ZO_dict) #chiama la funzione

#crea su text un array che separa ogni elemento quando incontra ciò che è scritto dentro split, 
# in questo caso lo spazio vuoto
text = text.split(" ") 
message = ""

for e in text:
    # int(e,2): converto in decimale ciè che è in binario:
    #   - 2: perché è in binario
    #   - e: il contenuto in posizione e dell'array che ho creato con lo split (tipo contiene 011 --> 3)
    # chr(int(e,2)): converto in ascii il valore decimale che ho ottenuto precedentemente
    message += chr(int(e,2))

#ottengo un messaggio con == alla fine, quindi è in base64, faccio il decode in base64, poi in utf-8
base64Decode = base64.b64decode(message)
print(base64Decode.decode('utf-8'))

# ho ottenuto un risultato che sembra un testo, ma non ha senso perché si è utilizzato il cifrario a lettere invertite
#(o come si chiama), allora, qui ti metti a pregare perché dura troppo, però pensa che la parola sptriz nellla flag la mette
# spesso e che puoi usare questo sito per analizzare le frequenze, in alto ci sono quelle più utilizzate nell'alfabeto inglese
# e sotto quelle più utilizzate nella tua frase https://www.101computing.net/frequency-analysis
# piano piano ottieni il risultato, se non riesci a trovarlo in tempo don't panic, basta che scrivi (anche in italiano) il
#procedimento che hai fatto fino a questo punto e cosa intendi fare, ti da tipo 9 punti su 12 (parole di m&m)

dizionario_testo= {'B':'s','N':'p','O':'r','R':'i','T':'t','U':'z','A':'o','W':'m','Q':'h','K':'a','E':'w','Y':'e','G':'n','S':'k','P':'v','Z':'y','X':'f','V':'d','F':'u','C':'c','J':'l','I':'g','H':'b','D':'j','L':'x'}

text_plain = replace_chars(base64Decode.decode('utf-8'), dizionario_testo)

print(text_plain)
#answer: spritz{shinra_tensei_everywhere}

#reminder anti panico, per seguire scrivi python nomees.py