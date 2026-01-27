n, m = map(int, input().split())
a = []
b = []
while n >= 0:
    a.append(4)
    n -= 4
    b.append(5)

a.append(5)
b.append(5)

print(*a, sep = "")
print(*b, sep = "")
