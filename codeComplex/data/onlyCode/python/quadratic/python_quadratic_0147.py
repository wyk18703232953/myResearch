n=int(input())
c=[0]*4
for k in range(4):
 for i in range(n):
  s=input()
  for j in range(n):
   if(i+j)%2!=int(s[j]):c[k]+=1
 if k<3:input()
c.sort()
print(c[0]+c[1]+2*n*n-c[2]-c[3])
