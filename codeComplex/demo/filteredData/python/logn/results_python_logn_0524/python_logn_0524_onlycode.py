

n = int(input())
x = 1
n -= 1
y = 9
while n > x * y:
    n -= x * y
    y *= 10
    x += 1
a = (8 + 2) ** (x - 1)
a += n // x
print(str(a)[n % x])