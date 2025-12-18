metto l'eseguibile su IDA e controllo il flusso del programma e faccio il decompiling in c:
- la prima cosa che chiede è il nome e vedo che deve essere ```SumitiLover1234```
- successivamente chiede di inserire il panino (suppongo sia fantasia, ma controllo) vedo che ogni carattere è controllato con un ascii, mettendolo in ordine e convertendolo vedo che il panino da indicare è: 70 52 110 84 97 53 49 65 -> ```F4nTa51A``` (ecco appunto)
- per l'ultimo pezzo è necessario il gdb perché non potendo fare patching, devo trovare il valore della variabile creata, quindi metto un breakpoin appena dopo la creazione, esattamente nel mov     [rbp+var_44], eax con indirizzo *0x0000555555555683, trovato facendo disasseble main. Posso farlo perché non ci sono ptrace che mi bloccano dall'utilizzare gdb. una volta fermato al breakpoin faccio print $eax e ottengo il pin (a questo giro ad esempio era 5387)

ho ottenuto la flag:
```Oh you did it!!! Here your wonderful panino:
SPRITZ{TwO_EuRo_PleAs3}```