n=int(input())
l=[int(i) for i in input().split()]
s=set(l)
if 0 in s:
    print(len(s)-1)
else:
    print(len(s))