l=list(map(int,input().split()))
l.sort()
x1=l[0]
x2=l[1]
x3=l[2]
if l[0]==1 or (l[0]==2 and l[1]==4 and l[2]==4) or (l[0]==3 and l[1]==3 and l[2]==3) or (l[0]==2 and l[1]==2):
    print("YES")
else:
    print("NO")