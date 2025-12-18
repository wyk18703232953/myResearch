l = list(sorted(list(map(int,input().split()))))
if min(l) == 1 or (l[0]==3 and l[1]==3 and l[2]==3) or (l[0]==2 and l[1]==4 and l[2]==4) or(l[0]==2 and l[1] == 2):
    print("Yes")
else:
    print("No")