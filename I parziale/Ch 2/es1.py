def main():
    stringa = input("Inserisci una stringa ")   
    print(f"input: {stringa}")

    risultato = ""

    for carattere in stringa:
        if carattere.isalpha(): #controllo che sia una lettera
            if carattere.isupper():
                base = ord('A')  
            else:
                base = ord('a')
        
            shift = (ord(carattere) - base + 2) %26 + base
            risultato += chr(shift)
        else:
            risultato += carattere

    print(f"output: {risultato}")

if __name__ == "__main__":
    main()