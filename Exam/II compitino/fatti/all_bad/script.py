from pwn import *

elf = ELF('./vuln')

target_address = elf.got['exit']
print ('target address:\t', hex(target_address))

#0x4012B6
#0x404050
