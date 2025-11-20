def xor(n1, n2):
    return bytes(i ^ j for i,j in zip(n1,n2))

#  `X1`: b840946f97ffe078ce6581d145ff3bd86cdfd0add863fc718300
#   `X2 ⊕ X1`: 34f5785a7e42586044a7fc15bd7eed3b1f71045f7ecc177b22e0
#   `X2 ⊕ X3`: f7a5269d0cf0804431df076ec7e00df66d4bc1593c99f6bfff86
#   `FLAG ⊕ X1 ⊕ X2 ⊕ X3`: 3c95c09bef751b579adff6e0eb6b69416fcb6391949f6bba01

# a xor b = c c xor a = b
x1 = bytes.fromhex("b840946f97ffe078ce6581d145ff3bd86cdfd0add863fc718300")
x2 = xor(bytes.fromhex("34f5785a7e42586044a7fc15bd7eed3b1f71045f7ecc177b22e0"), x1)
x3 = xor(bytes.fromhex("f7a5269d0cf0804431df076ec7e00df66d4bc1593c99f6bfff86"), x2)



flag = xor(x1,x2)
flag = xor(flag,x3)
flag = xor(flag,bytes.fromhex("3c95c09bef751b579adff6e0eb6b69416fcb6391949f6bba01"))

print(flag)