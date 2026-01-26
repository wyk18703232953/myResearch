import sys
input = sys.stdin.readline

n,k=map(int,input().split())

MIN=0
MAX=n

while True:
    ANS=(MIN+MAX)//2
    
    if (n-ANS)*(n-ANS+1)//2-ANS>k:
        MIN=ANS+1
    elif (n-ANS)*(n-ANS+1)//2-ANS<k:
        MAX=ANS-1
    else:
        print(ANS)
        break
