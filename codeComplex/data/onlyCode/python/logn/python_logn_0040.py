l,r=map(int,input().split())
s=bin(l)[2:]
t=bin(r)[2:]
z=max(len(s),len(t))
s='0'*(z-len(s))+s
t='0'*(z-len(t))+t
i=0
while i<z and s[i]==t[i]:
    i=i+1
print(pow(2,z-i)-1)