n,m=map(int, input().split())
for i in range(n):
    mt=input()
    if mt.count('B')!=0:
        print(mt.count('B')//2+i+1,mt.count('B')//2+mt.index('B')+1)
        break