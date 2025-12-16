# Define a randomic password generator.
# The password should contain 10 characters.
# Type of characters: alphanumeric

import random

def main():

    result = ""

    for n in range(10):
        random_pw = random.randint(0, 2) # 0 = lettera minuscola, 1 = lettera maiuscola, 2 = numero 
        if random_pw == 0:
            base = ord('a')
            result += chr(base + random.randint(0,25))
        elif random_pw == 1:
            base = ord('A')
            result += chr(base + random.randint(0,25))
        elif random_pw == 2:
            result += str(random.randint(0,9))

    print(f"password defined: {result}")

if __name__ == "__main__":
    main()