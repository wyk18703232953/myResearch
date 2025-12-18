n, m = map(int, input().split())
x1 = -1
x2 = -1
y1 = -1
y2 = -1
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == 'B':
            if x1 == -1:
                x1 = j + 1
            x2 = max(x2, j + 1)
            if y1 == -1:
                y1 = i + 1
            y2 = i + 1
print((y1 + y2) // 2, (x1 + x2) // 2)