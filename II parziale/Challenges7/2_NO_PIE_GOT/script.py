from pwn import *

elf = ELF('./vuln')
target_addressWin = elf.symbols['win']
target_addressExit = elf.got['exit']

print ('target addressWin:\t', target_addressWin)
print ('target addressExit:\t', target_addressExit)
