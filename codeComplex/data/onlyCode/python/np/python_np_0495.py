import sys
input = lambda: sys.stdin.readline().rstrip()
#CF-E-00
from collections import deque, defaultdict
def topological_sort(In, Out):
    dq, L = deque(), []
    for i, I in enumerate(In):
        if not I:
            dq.append(i)
    while dq:
        v = dq.popleft()
        L.append(v)
        for w in Out[v]:
            In[w].remove(v)
            if not In[w]:
                dq.append(w)
    if len(L) < len(In):
        return False
    return L

def main():
    n, m, k = map(int,input().split())  #k: length of following inputs

    def edges(s):
        Ans = set()
        for i in range(2**k):
            ans = ''
            for j in range(k):
                if i>>j&1:
                    ans = ''.join([ans, s[j]])
                else:
                    ans = ''.join([ans, '_'])
            Ans.add(ans)
        return Ans

    D = defaultdict(lambda : -1)
    for i in range(n):
        D[input()] = i

    flag = 1
    In, Out = [set() for _ in range(n)], [set() for _ in range(n)]
    for _ in range(m):
        S, t = input().split()
        t = int(t)

        for e in edges(S):
            if D[e]+1:
                Out[t-1].add(D[e])
                In[D[e]].add(t-1)
        if t-1 not in Out[t-1]:
            flag = 0
            break
        else:
            Out[t-1].remove(t-1)
            In[t-1].remove(t-1)

    T = topological_sort(In, Out)
    if flag == 0 or not T:
        print('NO')
    else:
        print('YES')
        print(*[t+1 for t in T], sep = ' ')
        
main()