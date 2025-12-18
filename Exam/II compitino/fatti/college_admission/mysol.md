il prolema era la funzione ptrace che mi impedita di utilizzare i breakpoint per trovare il valore generato randomicamente prima che mi venisse chiesto, quindi ho sostituito la funzione call ptrace con dei noi (una sequenza da 5 90) e la funzione si è disabilitata, ora posso utilizzare i break e trovare la flag:
- il nome è dato: ```Anya Forger, Park Avenue 128```
- il primo numero da selezionare è generato randomicamente, metto un break poin alla riga: ```0x401876``` una volta raggiunto faccio ```print $eax``` e mi mostra il numero 
- il secondo alla riga: ```0x4018db``` e faccio come prima
- poi ho modificato i salti da jle a jge per evitare di entrare in cicli che sarebbero durati minuti (quindi ho cambiato da 7E a 7D)

alla fine viene generato un file ```admission_result.txt``` contenente la flag:

```SPRITZ{Ez_D3J4Vu?!?!}```