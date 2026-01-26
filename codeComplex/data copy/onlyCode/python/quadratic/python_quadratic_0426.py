n=int(input())
a=int(input())

s=0
t=a
b=[]
for i in range(n):
    s+=t%10
    b.append(t%10)
    t//=10
    # print("***")
b.reverse()    
# print(b)
i=2
ans=False
# print(s)
if(s==0): ans=True
while(i<=s):
    # print(i)
    if(s%i!=0): 
        i+=1
        continue
    l=s//i
    c=0
    su=0
    for j in range(n):
        if(su>l):
            break
        else:
            su+=b[j]
            if(su==l):
                su=0
                c+=1
    if(c==i):
        ans=True
    # print(i,"**")    
    i+=1
if(ans): print("YES")
else:print("NO")