import random
import string


def transformation(input):
    input = list(input)
    input.append(input[0])
    input.pop(0)
    return "".join(input)
    #inverte il primo e l'ultimo
    #esempio: input -> inputi -> nputi


def reverse_transformation(input):
    input = list(input)
    input.insert(0, input[-1])
    input.pop()
    return "".join(input)
    # prende l'ultimo elemento e lo mette come primo
    #toglie di default l'ultimo elemento
    #esempio: input-> tinput -> tinpu


def encrypt(input, seed):
    input = transformation(input)
    input = list(input)
    random.seed(seed) #basato su un seed, non cambia
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    return input
    #ogni carattere dell'input è prima trasformato con transormation e poi
    # messo in xor con un numero generato randomicamente tra 80 e 120, tuttavia impostando
    # un seed, non sembra cambiare


def decrypt(input, seed):
    input = list(input)
    random.seed(seed) #basato su un seed, non cambia
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    input = reverse_transformation(input)
    input = reverse_transformation(input)
    return input


with open("secret.txt", "r") as file:
    cipher = file.read()

out = dict()
for seed in range(1000):
    decrypted = decrypt(cipher, seed)
    if "prit" in decrypted:
        print(seed, decrypted)
