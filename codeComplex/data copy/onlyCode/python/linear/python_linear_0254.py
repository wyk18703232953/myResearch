n, k = map(int, input().split())
print("YES")
for i in range(n):
    print(".", end = '')
print()
if k&1:
    if k <= n-2:
        tmp = (n-k)>>1
        for i in range(tmp):
            print(".", end = '')
        for i in range(k):
            print("#", end = '')
        for i in range(tmp):
            print(".", end = '')
        print()
        for i in range(n):
            print(".", end = '')
        print()
    else:
        print(".", end = '')
        for i in range(n-2):
            print("#", end = '')
        print(".")
        k -= n-2
        print(".", end = '')
        for i in range(k>>1):
            print("#", end = '')
        for i in range(n-k-2):
            print(".", end = '')
        for i in range(k>>1):
            print("#", end = '')
        print(".")
else:
    k = k>>1
    for j in range(2):
        print(".", end = '')
        for i in range(k):
            print("#", end = '')
        for i in range(n-k-1):
            print(".", end = '')
        print()
for i in range(n):
    print(".", end = '')
print()

