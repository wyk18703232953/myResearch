import math
n=int(input())
lst = list(map(int, input().strip().split(' ')))
s=input()
for j in range(n):
    lst[j]=[lst[j],j+1]
lst.sort()
stk=[]
i=0
for j in range(2*n):
    if s[j]=='0':
        stk.append(lst[i][1])
        print(lst[i][1],end=" ")
        i+=1
    
    else:
        print(stk[-1],end=" ")
        stk.pop()
        