# import sys
# input = sys.stdin.readline

n, q = map(int, input().split())
for _ in range(q):
    u = int(input())
    s = input()
    for comm in s:
        k = 1
        while True:
            if k & u:
                break
            k <<= 1
        if comm == 'L':
            if k != 1:
                u -= k
                u += (k>>1)
        elif comm == 'R':
            if k != 1:
                u += (k>>1)
        elif comm == 'U':
            nu = u - k
            nu |= (k<<1)
            if nu <= n:
                u = nu
    print(u)