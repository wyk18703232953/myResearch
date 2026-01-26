import io,os
# input = sys.stdin.buffer.readline
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n,m=map(lambda x:int(x), input().split())
A = []
for _ in range(n):
    scores = list(map(lambda x:int(x), input().split()))
    A.append(scores)

def solve(n,m,A):
    # O(31*( 5*n + 4**5 ))
    # all index from 0
    ans = ()
    nstats = 2**m
    def judge(finalScore):
        nonlocal ans
        seen = {}
        for i,scores in enumerate(A):
            sta = 0
            for e in scores:
                sta=sta*2+(e>=finalScore)
            # example [1,2,3,4,1], finalScore=3
            # sta = 0b00110
            seen[sta]=i
        
        for i in range(nstats):
            for j in range(nstats):
                if ((i|j) == nstats-1) and i in seen and j in seen:
                    ans = (seen[i], seen[j])
                    return True

        return False
    
    l=0
    r=2**31-1
    while l<r:
        m=l+(r-l)//2
        if not judge(m):
            r=m
        else:
            l=m+1
    # Highest score is l-1
    print(ans[0]+1,ans[1]+1) # answer index start from 1

solve(n,m,A)
