def solve():
    from sys import stdin
    f_i = stdin
    
    n = int(f_i.readline())
    
    segments = []
    for i in range(n):
        x, w = map(int, f_i.readline().split())
        segments.append((x + w, x - w)) # (end, start)
    segments.sort()
    
    ans = 0
    t = segments[0][1]
    for end, start in segments:
        if t <= start:
            ans += 1
            t = end
    
    print(ans)

solve()