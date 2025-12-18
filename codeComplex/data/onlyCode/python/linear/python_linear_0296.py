n=int(input())
l=list(map(int,input().split()))
s=set(l)
x=0
if x in s:
    print(len(s)-1)
else:
    print(len(s))