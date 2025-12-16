from collections import Counter

def analyze_redundancy(text):
    top = 10
    # --------------------------
    # Lettere singole
    # --------------------------
    letters = [c for c in text if c.isalpha()]  # consideriamo solo lettere
    letter_counts = Counter(letters)
    most_common_letters = letter_counts.most_common(top)  # lista ordinata
    print("=== Lettere più frequenti ===")
    for letter, count in most_common_letters:
        print(f"{letter}: {count}")

    # --------------------------
    # Digrammi (coppie)
    # --------------------------
    digrams = [text[i:i+2] for i in range(len(text)-1)]
    digram_counts = Counter(digrams)
    most_common_digrams = digram_counts.most_common(top)
    print("\n=== Digrammi più frequenti ===")
    for digram, count in most_common_digrams:
        print(f"{digram}: {count}")

    # --------------------------
    # Trigrammi (triple)
    # --------------------------
    trigrams = [text[i:i+3] for i in range(len(text)-2)]
    trigram_counts = Counter(trigrams)
    most_common_trigrams = trigram_counts.most_common(top)
    print("\n=== Trigrammi più frequenti ===")
    for trigram, count in most_common_trigrams:
        print(f"{trigram}: {count}")

    # --------------------------
    # Ritorno delle liste ordinate (opzionale)
    # --------------------------
    return most_common_letters, most_common_digrams, most_common_trigrams



def main():
    text = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"
    analyze_redundancy(text)

    dec = ""
    for i in text:
        if i == "N":
            dec += "t"
        elif i == "L":
            dec += "h"
        elif i == "U":
            dec += "e"
        elif i == "K":
            dec += "i"
        elif i == "Q":
            dec += "m"
        elif i == "B":
            dec += "s"
        elif i == "D":
            dec += "o"
        elif i == "C":
            dec += "r"
        elif i == "X":
            dec += "c"
        elif i == "T":
            dec += "u"
        elif i == "P":
            dec += "y"
        elif i == "G":
            dec += "d"
        elif i == "V":
            dec += "w"
        elif i == "M":
            dec += "n"
        elif i == "W":
            dec += "f"
        elif i == "I":
            dec += "g"
        elif i == "J":
            dec += "p"
        elif i == "F":
            dec += "a"
        elif i == "A":
            dec += "l"
        elif i == "S":
            dec += "v"
        elif i == "H":
            dec += "b"

        else:
            dec +=i
    
    print (text)
    print (dec)

    # K è una vocale
    # F è una vocale
    # D è una vocale
    # M o U è una vocale
    # W è una consonante

if __name__ == "__main__":
    main()