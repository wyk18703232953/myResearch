n = int(input())
a = [0] * (n+1) ; b = [0] * (n+1) ; c = [0] * (n+1)
for i in range(2, n+1):
    a[i] = int(input())
    b[a[i]] += 1
for i in range(1, n+1):
    if b[i] == 0:
        c[a[i]] += 1
for i in range(1, n+1):
    if b[i] != 0 and c[i] < 3:
        print("NO")
        exit()
print("YES")