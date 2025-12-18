n, k = map(int, input().split())
if n == 1:
    print(0)
elif (k*k -k)//2 +1 < n:
    print(-1)
else:
    g, b = 0, k//2
    while b != 0:
        while g +b <= k and (k*k -k)//2 +1 -((g +b)**2 -(g +b))//2 >= n:
            g += b
        b //= 2
    print(k -g)
