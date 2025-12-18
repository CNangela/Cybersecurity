ho guardato l'eseguibile in IDA e ho scoperto che l'user doveva essere UniPD_Student, mentre per la password c'era una funzione apposta che controllava i caratteri inseriti, doveva essere di esattamente 8 caratteri e ogni carattere era confrontato con un ascii, convertendo da ascii a text nell'ordine della stringa da inserire, scopro che la password è P10v3go! 
Resta da scoprire solo il PIN, questo è creato randomicamente, da IDA non era possibile scoprirlo, quindi sono andata sul gdb, ho fatto:
- b main
- run
- disassemble main
ho guardato confrontandomi con IDA dov'era il punto in cui veniva creato il PIN e ho esso un break
```b* 0x401537``` questa variabile non aveva un nome, era semplicemente allocata nello stack e il suo registro era eax, quindi una volta arrivato all'indirizzo di breakpoint ho scritto ```print $eax``` e mi ha dato il pin creato nella funzione appena passata, la flag è 

SPRITZ{P00r_45_DuCk}