import string

a = list(string.ascii_letters + string.punctuation)

def verify(msg, a):
    for c in list(msg):
        if c not in a:
            raise Exception("Invalid character")

def encrypt(msg, k):
    verify(msg, a)

    msg = list(msg)

    for i in range(len(msg)):
        in_ = msg[i]
        idx_in = a.index(in_)
        idx_out = (idx_in + k) % len(a)
        out_ = a[idx_out]
        msg[i] = out_

    return "".join(msg)

def decript(msg,k):

    verify(msg, a)

    msg = list(msg)

    for i in range(len(msg)):
        in_ = msg[i]
        idx_in = a.index(in_)
        idx_out = (idx_in - k) % len(a)
        out_ = a[idx_out]
        msg[i] = out_

    return "".join(msg)


cipher = "XuywnEHYKbny~Bfx~tsqD~f~xnruqj~hnumjwd"

print(decript(cipher,5 ))

for k in range(-10000, 10000):
    dec = decript(cipher, k)
    if "Spritz" in dec:
        print("chiave", k)
        print(dec)
        break

# plaintext = " unknown"
# cipher = encrypt(plaintext, 5)
