n = int(input())-1
x = 1
y = 9
while n > x * y:
    n -= x * y
    y *= 10
    x += 1
a = 10 ** (x - 1)
a += n // x
print(str(a)[n % x])