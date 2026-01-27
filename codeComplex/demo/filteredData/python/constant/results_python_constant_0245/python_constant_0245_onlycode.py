n = int(input())
m = int(input())
r = 1
for power in range(n):
    r *= 2
    if r > m:
        print(m)
        break
else:
    if r == m:
        print(0)
    else:
        print(m % r)
