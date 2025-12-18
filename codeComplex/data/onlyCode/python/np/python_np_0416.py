import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
n,m = map(int, input().split())
a = []
for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)
 
def check(mid):
    mask = (1<<m)-1
    s = set()
    d = dict()
    for i in range(n):
        state = 0
        for j in range(m):
            if a[i][j] >= mid:
                state += 1<<j
        #if state!=0:
            #print("1bin",bin(state),mid,a[i])
        if state in s:
            continue
        s.add(state)
        k = state
        while k>=0:
            #print(k,state)
            k &= state
            d[k] = i
            k -= 1
        need = mask^state
        #print(s,d,need,state)
        if need in d:
            q1, q2 = d[need], i
            if q1 > q2:
                q1, q2 = q2, q1
            return True, (q1, q2)
    #print(s,d,need,bin(state))
    return False, (-1, -1)
 
left = 0
right = 10**9+1
i,j = 0, 0
while right-left>1:
    mid = (right+left)//2
    flag, (q1, q2) = check(mid)
    #print("resround",mid,left,right,i,j,q1,q2)
    if flag:
        left = mid
        i,j = q1, q2
    else:
        right = mid
print(i+1, j+1)
 
