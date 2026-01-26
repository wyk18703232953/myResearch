n=int(input())
s=(input())
L=s.split(" ")
L=list(set(L))
for i in range(len(L)):
    L[i]=int(L[i])
L=sorted(L)
if len(L)==1:
    print("NO")
else:
    print(L[1])
