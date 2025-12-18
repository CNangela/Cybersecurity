dovevo mettere come primo indirizzo la funzione da sostituire e come secondo la funzione con cui l'avrei voluto sostituire, questo è possibile grazie al codice *pointer = temp;
- prima l'indirizzo di pointer cambia inserendo quello che voglio sostituire grazie allo  __isoc99_scanf("%d", &pointer);
- poi inserisco l'indirizzo di quello che voglio ottenere gtazie a __isoc99_scanf("%d", &temp); 

ora l'indirizzo di pointer è quello che ho indicato (la funzione exit) e il suo valore è quello presente nella cella di memoria con il secondo indirizzo immesso (show_true_ending)

lascio il codice py:
```
from pwn import *

elf = ELF('./vuln')

target_addressExit = elf.got['exit']
target_addressSTE = elf.symbols['show_true_ending']
print ('target addressExit:\t', target_addressExit)
print ('target addressSTE:\t', target_addressSTE)
```
la flag è
```SPRITZ{GoT_Hijacking_iS_FUn{flag}}\n\n'```

## spiegazione del codice
- con elf.got ottengo l'indirizzo (decimale, perché dovevo immettere un numero e quindi non poteva essere hex) della cella di memoria con la funzione che contiene il nome 'exit'. Devo utilizzare got perché exit sta in un area di memoria diversa da quella del codice. ottengo -> 4210784
- con elf-symbles è la stessa cosa, ma mi sevr per aree di memoria che comprendono il codice. ottengo -> 4198839

ottenute questi due indirizzi, li do come input (prima 4210784 e poi 4198839) al programma e ottengo la flag sopracitata