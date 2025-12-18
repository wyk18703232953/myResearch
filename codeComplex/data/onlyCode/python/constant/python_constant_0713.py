n, k = [int(x) for x in input().split()]
if k == 1:
    print("1" + "0"*(n-1))
else:
    tmp = "0" * ((n-k)//2) + "1"
    s = tmp
    s = tmp * (n // len(tmp) + 1)
    s = s[:n]
    print(s)