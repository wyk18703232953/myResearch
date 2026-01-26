n = int(input())
if n == 0:
    print(0, 0, 0)
else:
    a, b = 0, 1
    while a + b != n:
        a, b = b, a + b
    print(0, a, b)