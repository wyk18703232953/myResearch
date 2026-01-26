n,m=map(int,input().split())
seq=list(map(str,input().split()))
fp=list(map(str,input().split()))
checklist=[]
for number in seq:
    if(number in fp):
        checklist.append(number)
print(" ".join(checklist))