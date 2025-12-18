c'era da fare il patch su IDA, quindi ho importato l'eseguibile e ho controllato il flusso del programma, di seguito riporto le modifiche fatte:
- modificato jz con jzn per il controllo test eax perché non mi permetteva di inserire l'input (ma sarebbe stato ```Dwight Schrute, position Assistant to the regional manager```) qui si va a modificare 74 con 75
- andava a generare un numero randomico tra 0 e 4, non potendolo prevedere ho modificato jz con jzn e immesso un input > 4
- ho modificato i due jle con jge perché altrimenti da 0 si sarebbe dovuto incremnetare la variabile di volta in volta fino a raggiungere 95h, inoltre si chiamava una funzione di sleep, quindi avrebbe rallentato di 149 secondi il prossimo passaggio, che si comportava allo stesso modo, quindi avrei dovuto aspettare aspettare più di 4 minuti per una risposta. La modifica consiste da 7E a 7D

ho ottenuto la flag:
```spritz{th4ts_wh4t_sh3_s41d}```