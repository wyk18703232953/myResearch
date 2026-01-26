l, r = list(map(int, input().strip().split()))

if l == r:
    print(0)
    exit()

l, r = bin(l)[2:].zfill(64), bin(r)[2:].zfill(64)
i = 0
while i < len(r):
    if l[i] == r[i]:
        i += 1
    else:
        break
rslt = len(r[:i])*'0' + len(r[i:])*'1'
print(int(rslt, 2))
