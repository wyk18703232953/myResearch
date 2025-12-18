n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [0] * n
for i in a:
    b[i - 1] += 1
b.sort()
print(b[0])
