print('?', 0, 0, flush=True)
t = int(input())
s = [0]*31
if t == 1:
    s[30] = 1
else:
    s[30] = -1

a = 0
b = 0
for i in range(30, 0, -1):
    c = (1 << (i-1)) + a
    d = b
    print('?', c, d, flush=True)
    ans1 = int(input())
    c = a
    d = (1 << (i-1)) + b
    print('?', c, d, flush=True)
    ans2 = int(input())
    if ans1 == -1 and ans2 == 1:
        a += 1 << (i-1)
        b += 1 << (i-1)
        s[i-1] = s[i]
    elif ans1 == 1 and ans2 == -1:
        a += 0 << (i-1)
        b += 0 << (i-1)
        s[i-1] = s[i]
    else:
        s[i-1] = ans1
        if s[i] == 1:
            a += 1 << (i-1)
            b += 0 << (i-1)
        else:
            a += 0 << (i-1)
            b += 1 << (i-1)
print('!', a, b)

