tramite questo script in python 
```
from pwn import *
target_address = p64(0x4005C7) 
garbage =  b'a'*(28+4+8) 
msgin = garbage + target_address 
p = process('./easy_bof') 
p.sendline(msgin) 
p.interactive()
```

ho ottenuto la flag:
```
Congratz! You win the flag: spritz{bof_for_fun_and_profit?}
```

## come funziona:
ho messo l'eseguibile su IDA e ho trovato la password corretta, tuttavia questa mi avrebbe solo risposto con Correct Password, non c'erano chiamate alla funzione per stampare la flag; quindi ho cercato la funzione che l'avrebbe stampata, ovvero _getFlag()_ e ho guardato al suo indirizzo che è _0x4005C7_.\
Noto che per stampare Correct Password si è utilizzato un puts, perfetto per richiamare una funzione a mia scelta. \
L'idea è quella di consumare il buffer e metterci di seguito la chiamata alla funzione per stampare la flag, faccio i conti dei byte:
- buff[28] quindi 28 byte sono per buff, ma i blocchi sono da 16, quindi ne aggiungo 4 per arrivare a 32 e colmare il vuoto con il padding
- aggiungo altri 8 di base pointer dato che siamo a 64bit e infine la flag che è anch'essa di 8 byte, arrivando a 16 perfetti\

eseguo il codice e ottengo la flag