from pwn import *
elf = ELF('./auth')
target_addressWin = elf.symbols['win']
target_addressExit = elf.got['exit']
print ('target addressWin:\t', hex(target_addressWin))
print ('target addressExit:\t', hex(target_addressExit))