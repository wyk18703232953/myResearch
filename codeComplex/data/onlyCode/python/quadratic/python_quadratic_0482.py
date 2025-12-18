n = int(input())
L = [int(i) for i in input().split()]
R = [int(i) for i in input().split()]
E = []
otv = [0] * n
for i in range(n):
    sum_ = L[i] + R[i]
    E.append([sum_, i])
E.sort()
for i in range(n):
    x = R[i]
    for j in range(n):
        if (x > 0):
            if (E[j][1] > i):
                otv[E[j][1]] += 1
                x -= 1
        else:
            break
        
    if (x > 0):
        print("NO")
        exit()
        
    x = L[i]
    for j in range(n):
        if (x > 0):
            if (E[j][1] < i):
                otv[E[j][1]] += 1
                x -= 1
        else:
            break
        
    if (x > 0):
        print("NO")
        exit()

for i in range(n):
    r = 0
    l = 0
    for j in range(i + 1, n):
        if (otv[j] > otv[i]):
            r += 1
    for z in range(i - 1, -1, -1):
        if (otv[z] > otv[i]):
            l += 1
    if (r != R[i]) or (l != L[i]):
        print("NO")
        exit()

print("YES")
for i in range(n):
    print(otv[i] + 1, end = ' ')
    
    

