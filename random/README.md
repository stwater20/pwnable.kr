# random


rand() 特性 屬於偽隨機 沒有srand()當種子所以每次rand()結果會相同

(key ^ random) == 0xdeadbeef 

key ^ 0x6b8b4567 == 0xdeadbeef

key = 3039230856

```
random@pwnable:~$ echo  $((0x6b8b4567 ^ 0xdeadbeef))
3039230856
```

```

random@pwnable:~$ gdb -q random
Reading symbols from random...(no debugging symbols found)...done.
(gdb) disas main
Dump of assembler code for function main:
   0x00000000004005f4 <+0>:	push   %rbp
   0x00000000004005f5 <+1>:	mov    %rsp,%rbp
   0x00000000004005f8 <+4>:	sub    $0x10,%rsp
   0x00000000004005fc <+8>:	mov    $0x0,%eax
   0x0000000000400601 <+13>:	callq  0x400500 <rand@plt>
   0x0000000000400606 <+18>:	mov    %eax,-0x4(%rbp)
   0x0000000000400609 <+21>:	movl   $0x0,-0x8(%rbp)
   0x0000000000400610 <+28>:	mov    $0x400760,%eax
   0x0000000000400615 <+33>:	lea    -0x8(%rbp),%rdx
   0x0000000000400619 <+37>:	mov    %rdx,%rsi
   0x000000000040061c <+40>:	mov    %rax,%rdi
   0x000000000040061f <+43>:	mov    $0x0,%eax
   0x0000000000400624 <+48>:	callq  0x4004f0 <__isoc99_scanf@plt>
   0x0000000000400629 <+53>:	mov    -0x8(%rbp),%eax
   0x000000000040062c <+56>:	xor    -0x4(%rbp),%eax
   0x000000000040062f <+59>:	cmp    $0xdeadbeef,%eax
   0x0000000000400634 <+64>:	jne    0x400656 <main+98>
   0x0000000000400636 <+66>:	mov    $0x400763,%edi
   0x000000000040063b <+71>:	callq  0x4004c0 <puts@plt>
   0x0000000000400640 <+76>:	mov    $0x400769,%edi
   0x0000000000400645 <+81>:	mov    $0x0,%eax
   0x000000000040064a <+86>:	callq  0x4004d0 <system@plt>
---Type <return> to continue, or q <return> to quit---
   0x000000000040064f <+91>:	mov    $0x0,%eax
   0x0000000000400654 <+96>:	jmp    0x400665 <main+113>
   0x0000000000400656 <+98>:	mov    $0x400778,%edi
   0x000000000040065b <+103>:	callq  0x4004c0 <puts@plt>
   0x0000000000400660 <+108>:	mov    $0x0,%eax
   0x0000000000400665 <+113>:	leaveq 
   0x0000000000400666 <+114>:	retq   
End of assembler dump.
(gdb) 
(gdb) b *0x40062f
Breakpoint 1 at 0x40062f
(gdb) r
Starting program: /home/random/random 

(gdb) x/10x $rbp-4
0x7ffd4799047c:	0x6b8b4567	0x00400670	0x00000000	0x7854d840
0x7ffd4799048c:	0x00007fce	0x00000001	0x00000000	0x47990568
0x7ffd4799049c:	0x00007ffd	0x78b1cca0



```

```
random@pwnable:~$ ./random 
3039230856
Good!
Mommy, I thought libc random is unpredictable...
```