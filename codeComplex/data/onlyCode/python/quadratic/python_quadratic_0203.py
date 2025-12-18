n, m = map(int,input().split())
X = []
for i in range(n):
    a = input()
    U = [char for char in a]
    X.append(U)
nums = []
for i in range(m):
    t = 0 
    for j in range(n):
        t += int(X[j][i])
    nums.append(t)

for i in range(n):
    ok = True 
    for j in range(m):
        if X[i][j] == '1':
            if nums[j]>1:
                continue 
            else:
                ok = False 
    if ok == True:
        print("YES")
        quit()
print("NO")