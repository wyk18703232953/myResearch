def solve():
    l, r = map(int, input().split())
    
    ans = l^r
    j = 0
    while 1<<j <= ans:
        ans |= 1<<j
        j += 1

    print(ans)

solve()

