from pwn import *

elf = ELF('./vuln')

target_addressExit = elf.got['exit']
target_addressSTE = elf.symbols['show_true_ending']
print ('target addressExit:\t', target_addressExit)
print ('target addressSTE:\t', target_addressSTE)

#SPRITZ{GoT_Hijacking_iS_FUn{flag}}\n\n'