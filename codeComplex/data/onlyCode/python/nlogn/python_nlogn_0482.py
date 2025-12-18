n,k=map(int,input().split())
a=list(map(int,input().split()))
d={}
for chr in a:
     if chr not in d:
        d[chr]=1
     else:
        d[chr]+=1
p=list(d.values())
z=k//n
if z==0 :
     print(0)
else:
     o=[]
     if len(a)>=n:
        o.append(1)
     for i in range(2,z+1):
         c=0
         for j in range(len(p)):
             c+=p[j]//i
         if c>=n:
             o.append(i)
     print(max(o))