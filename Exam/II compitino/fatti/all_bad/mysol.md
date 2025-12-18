io l'ho fatto in modo diverso da quanto indicato nella soluzione del prof.

Ho messo l'eseguibile su IDA e ho guardato cosa faceva lo pseudocodice:
- inizialmente la prima cosa da inserire era 'y', in caso contrario il programma si sarebbe chiuso con un messaggio di ```Ooook bye :(```
successivamente ho notato che i due input da digitare dovevano necessariamente essere due numeri (dato l'utilizzo di %d nello scanf)
- alla fine del codice ho notato che il primo numero inserito doveva essere l'indirizzo della funzione da chiamare, mentre il secondo doveva essere l'indirizzo della cella da modificare con il primo inserito (*pointer = temp;)
- ho quindi cercato i due indirizzi da inserire:
    - per il primo dovevo trovare una funzione che mi stampasse la flag e ho notato una funzione chiamata give_the_man_a_guitar, aprendolo ho notato una sostituzione del file temp con un'immagine chiamata flag.png, la flag deve trovarsi li, quindi devo eseguire questa funzione. mi sono posizionata con il puntatore sullal chiamata alla funzione e premento spazio ho cercato il suo indirizzo -> primo indirizzo trovato! era 0x4012B6
    - per il secondo ho scritto uno script in python per trovare l'indirizzo della funzione exit() (cosa che avrei potuto fare anche per la funzione precedente una volta trovato il suo nome) e con elf.got['exit'] ho ottenuto il suo indirizzo -> 0x404050
- problema: sono richiesti input numerici interi, mentre i due indirizzi sono in hex, quindi ho usato un tool online per trovare il decimale:
    - funzione della flag: 4199094
    - exit: 4210768

input corretti, il programma mi ha stampato

> Thanks, I'll write now! Let's see if the magic happens:\
Oh you want to give him a guitar? What a BRILLIANT IDEA!\
As we thought, he made a beautiful song!!!\
https://youtu.be/zB_q1I0leoI?t=15\
He also left a picture of his angryness as little gift for you! Check it in the exercise folder! :)

guardando nella cartella ho trovato l'immagine con domenico bini e la flag: ```SPRITZ{St4nDndTTM4L3}```