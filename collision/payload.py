from pwn import *

payload = p32(0x6c5cec8) * 4 + p32(0x6c5cecc)

r = ssh('col' ,'pwnable.kr' ,password='guest', port=2222)
p = r.process(executable='./col', argv=['col',payload])
flag = p.recv()
print("Flag: " + flag.decode("utf-8"))
p.close()
r.close()