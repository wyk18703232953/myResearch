n, m = int(input()), int(input())
value = False
for j in range(n + 1):
    if pow(2, j) > m:
        value = True
        break
if value:
    print(m)
else:
    print(m % pow(2, n))