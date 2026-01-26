a, b= map(int,input().split())

if a == b:
    print(0)

else:
    x = a ^ b
    c = 0

    while x:
        x //= 2
        c += 1

    print(2**c-1)