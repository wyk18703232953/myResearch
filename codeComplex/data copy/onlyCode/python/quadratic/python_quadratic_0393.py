n,m=map(int,input().split())
lock=0
for i in range(n):
    s=str(input())
    if(('B' in s) and (lock==0)):
        Rstart=s.index('B')
        cnt=s.count('B')
        Rcen=Rstart+(cnt//2)
        Cstart=i
        Ccen=Cstart+(cnt//2)
        lock=1
        
print(Ccen+1,Rcen+1)        
        
        