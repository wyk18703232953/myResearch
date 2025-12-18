n = int(input())
m = int(n**.5)
a = []
 
for i in range(0, n, m):
    for j in range(i, min(i+m, n)):
        a.append(min(i+m, n)-j + i)
 
print(' '.join(str(_) for _ in a))