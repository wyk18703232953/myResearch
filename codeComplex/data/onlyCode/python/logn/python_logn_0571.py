n = int(input())
x, y = 1, 9
n -= 1
while n > x * y:
    n -= x * y
    x += 1
    y *= 10
a = 10 ** (x - 1) + n // x
print(str(a)[n % x])