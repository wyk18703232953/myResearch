n,m = map(int,input().split())
li = [[j for j in input()] for i in range(n)]
position1=0
position2=0
position3=0
position4=0
for j in range(m):
    flag = False
    for i in range(n):
        if li[i][j] == "B":
            flag = True
            position1 = i
            break
    if(flag == True):
        break
for j in range(m-1,-1,-1):
    flag = False
    for i in range(n-1,-1,-1):
        if li[i][j] == "B":
            flag = True
            position2 = i
            break
    if(flag == True):
        break
for i in range(n):
    flag = False
    for j in range(m):
        if li[i][j] == "B":
            flag = True
            position3 = j
            break
    if(flag == True):
        break
for i in range(n-1,-1,-1):
    flag = False
    for j in range(m-1,-1,-1):
        if li[i][j] == "B":
            flag = True
            position4 = j
            break
    if(flag == True):
        break

avg1 = (position1+position2)//2 + 1
avg2 = (position3 + position4)//2 + 1
print(avg1,avg2)
# print(li)