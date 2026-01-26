import math
t=1
while t:
        t-=1
        n=int(input())
        m=int(input()) 
        if(n>=27):
                print(m)
        else:
                print(m%(pow(2,n)))
