from collections import Counter

def replace_chars(text, dict):
    replaced_text = ""
    for c in text: 
        replaced_text += dict.get(c, c)

    return replaced_text

# mi serve per vedere la ridondanza delle lettere
def analyze_redundancy(text):
    top = 26
    # --------------------------
    # Lettere singole
    # --------------------------
    letters = [c for c in text if c.isalpha()]  # consideriamo solo lettere
    letter_counts = Counter(letters)
    most_common_letters = letter_counts.most_common(top)  # lista ordinata
    print("=== Lettere più frequenti ===")
    for letter, count in most_common_letters:
        print(f"{letter}: {count}")

with open("challenge.txt", "r") as f:
    text = f.read()
    f.close()

analyze_redundancy(text)

#vabe, spritz è sempre l'inizio della flag
dizionario_testo= {
    'D':'s',
    'M':'p',
    'P':'r',
    'X':'i',
    'S':'t',
    'T':'z',
    'L':'e',
    'A':'h',
    'Z':'c',
    'O':'n',
    'H':'a',
    'V':'f',
    'Y':'d',
    'R':'u',
    'W':'g',
    'Q':'k',
    'U':'l',
    'E':'o'}

print(replace_chars(text,dizionario_testo))
