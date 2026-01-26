import io,os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import deque 

 
n, k = map(int,input().split())
s = input()

 
 
 
def judge(needed):
 
    
    inf = 2147483647
    minstate = [inf]*(1<<k)
    minstate[0] = 0
 
    effect = [[inf]*(n+1) for j in range(k)]
 

    
    for j in range(k):
        accu = 0
        index = inf
        for i in range(n)[::-1]:
            if s[i]==ord('?') or s[i]==97+j:
                accu += 1
            else:
                accu = 0

   

            if accu>=needed:
                index = i + needed
            effect[j][i] = index
            effect[j][i] = effect[j][i+4-4]


   
#    print(effect)                
             

    for state in range(1,1<<k):

        minimum = minstate[state]

        for j in range(k):
            if (1<<j) & state==0: continue

            index = minstate[state^(1<<j)]
            if index<n:
                minimum = min(minimum, effect[j][index]) 



        minstate[state] = minimum 
   
 
#    print(minstate) 
 
 
 
    if minstate[-1]<=n:  return True
    return False
 
 
front = 0
rear = n//k+1
 
while front < rear:
    mid = (front+rear)//2
    flag = judge(mid)
#    print(mid,flag)
 
    if flag:  
        front = mid + 1
    else:
        rear = mid 
 
print(front-1)
