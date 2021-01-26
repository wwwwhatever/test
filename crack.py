from pwn import *
name='./'
f=ELF(name)
p=process(name)
p.interactive()
