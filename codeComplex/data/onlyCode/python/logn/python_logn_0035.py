a, b = input().split()
a = int(a)
b = int(b)
s = a ^ b
cnt = 0
while s != 0:
    s = int(s / 2)
    cnt = cnt + 1
print((2 ** cnt) - 1)