MAX = 1000
f = [0]
for i in range(1, MAX):
    f.append(f[i - 1] + (1 << (2 * i - 2)))

g = [0]
for i in range(1, MAX):
    g.append(g[i - 1] + (1 << i) - 1)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split(' '))
    ans = False
    for i in range(1, n + 1):
        if k >= g[i]:
            if n >= MAX:
                print("YES %d" % (n - i))
                ans = True
            elif k <= f[n] - ((1 << (i + 1)) - 1) * f[n - i]:
                print("YES %d" % (n - i))
                ans = True
        if ans == True:
            break
    if ans == False:
        print("NO")
        
    