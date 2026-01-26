n = int(input())
l = list(map(int,input().split()))
c1 = 0
c2 = 0
for i in l:
    if i % 2 == 0:
        c1+=1
    else:
        c2+=1
            
for i in range(len(l)-1,-1,-1):
    if l[i] % 2 == 0:
        lasteven = i
        break
for i in range(len(l)-1,-1,-1):
    if l[i] % 2 != 0:
        lastodd = i
        break
if c1 == 1:
    print(lasteven + 1)
else:
    print(lastodd + 1)
