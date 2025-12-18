from pwn import *
elf = ELF('./NeedsToBeHappy')

targetAddressExit = elf.got['exit']
targetAddressFlag = elf.symbols['give_the_man_a_cat']
print('targetExit:\t', targetAddressExit)
print('targetFlag:\t', targetAddressFlag)

# targetExit:      4210760
# targetFlag:      4199030

