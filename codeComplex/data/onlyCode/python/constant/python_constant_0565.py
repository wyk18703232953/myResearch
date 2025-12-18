n, m, k, l = map(int, input().split())
if m > n:
    print(-1)
elif l + k > n:
    print(-1)
else:
    s = (l + k) // m + bool((l + k) % m)
    if s * m > n:
        print(-1)
    else:
        print(s)
