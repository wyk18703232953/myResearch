import sys
input = sys.stdin.buffer.readline 

def process(A):
    d = {}
    final = set([])
    for x in A:
        if x not in d:
            d[x] = 0
        d[x]+=1
        if d[x] >= 4:
            return [x, x, x, x]
        if d[x] >= 2:
            final.add(x)
    L = sorted(final)
    answer = [float('inf'), None, None]
    for i in range(len(L)-1):
        a = L[i]
        b = L[i+1]
        a1 = a/b+b/a
        answer = min(answer, [a1, a, b])
    a1, a, b = answer
    return [a, a, b, b]
 
t = int(input())
for i in range(t):
    n = int(input())
    A = [int(x) for x in input().split()]
    a, b, c, d = process(A)
    print(f'{a} {b} {c} {d}')