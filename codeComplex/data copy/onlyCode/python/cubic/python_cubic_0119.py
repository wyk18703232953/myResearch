import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def solve2(s, t, left, right):
    n = len(s)
    m = len(t)
    nuxt = [-1]*(left+1)
    nuxt[0] = 0

    for i in range(n):
        for j in reversed(range(left+1)):
            k = nuxt[j]
            if k == -1:
                continue
            if j != left:
                if s[i] == t[j]:
                    nuxt[j+1] = max(nuxt[j+1], k)
            if k != right:
                if s[i] == t[left+k]:
                    nuxt[j] = max(nuxt[j], k+1)
    return nuxt[-1]==right

def solve():
    s = input()
    t = input()
    m = len(t)
    for i in range(m+1):
        if solve2(s,t,i,m-i):
            print("YES")
            return
    print("NO")

t = int(input())
for i in range(t):
    solve()

