l,r=map(int,input().split())
p=bin(l)
p=p[2:]
q=bin(r)
q=q[2:]

t=len(q)
u=len(p)
p=(t-u)*'0'+p
ans=[]

for i in range(len(q)):
    if(q[i]=='1' and p[i]=='0'):
        ans.append(1)
        break;
    elif(q[i]=='1' and p[i]=='1'):
        ans.append(0)
        continue;
    elif(q[i]=='0' and p[i]=='1'):
        ans.append(1)
        continue;
    else:
        ans.append(0)
for j in range(i+1,len(p)):
        ans.append(1)
total=0

ans.reverse()


for i in range(len(ans)):
    total+=pow(2,i)*ans[i]

print(total)


