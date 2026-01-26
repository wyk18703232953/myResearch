n=int(input())
l=[4,7,47,74,44,77,447,444,474,777,747,744,477]
c=0
for i in range(len(l)):
    if n%l[i]==0:
        c=1
        break
if c==1:
    print("YES")
else:
    print("NO")
