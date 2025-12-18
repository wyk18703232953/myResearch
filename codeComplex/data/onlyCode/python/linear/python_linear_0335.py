a,b = map(int,input().split())
d = list(map(int,input().split()))
e = []
e1= []
mx = 0
current = 0
for i in range(len(d)):
    if i%2 == 0:
        e.append(d[i]-current)
    else:
        e1.append(d[i]-current)
    current=d[i]
if i%2 == 0:
    e1.append(b-current)
else:
    e.append(b-current)
mx = sum(e)
su = 0
su2 = sum(e1)
for i in range(len(e)):
    su+=e[i]
    mx = max(mx,su+su2-1)
    try:
        su2-=e1[i]
    except:
        break
print(mx)
    
