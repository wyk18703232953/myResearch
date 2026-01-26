n, s = map(int, input().split())
 
a, b, c = 0, n + 1, 0
 
while a < b:
    c = (a + b) // 2
    if c - sum([int(x) for x in str(c)]) < s:
        a = c + 1
    else:
        b = c
 
print(n - b + 1)