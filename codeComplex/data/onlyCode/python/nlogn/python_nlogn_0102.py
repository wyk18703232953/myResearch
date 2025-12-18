nab=input().split()
l=input().split()
nab=[int(i) for i in nab]
l=[int(i) for i in l]
l.sort()
if(l[nab[2]-1]==l[nab[2]]):
    print(0)
else:
    print(l[nab[2]]-l[nab[2]-1])
