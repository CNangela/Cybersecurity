from pwn import *

elf = ELF('./goat')

target_addressExit = elf.got['exit']
target_addressWin = elf.symbols['win']
print ('target address:\t', hex(target_addressExit))
print ('target address:\t', hex(target_addressWin))

# target address:  0x804c018
# target address:  0x80491c6