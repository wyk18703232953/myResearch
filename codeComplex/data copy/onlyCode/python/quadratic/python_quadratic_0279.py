n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
out=[]
first=11
for a in range(len(x)):
    for b in range(len(y)):
        #print(a,b,end=" ")
        if y[b]==x[a]:
            if first<a:
                first=a;
                out.append(y[b])
                #print(1,first,out,x[a],y[b])
                b+=1
                
            else:
                out.insert(0,y[b])
                #print(2,first,out,x[a],y[b])
                b+=1
                
        else:
            
           # print(first,out,x[a],y[b])
            b+=1
out.reverse()
for a in out:
    print(a)