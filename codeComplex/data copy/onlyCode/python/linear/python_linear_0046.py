def process(X, a, b):
    X1 = set(X)
    Other = set([])
    A = set([])
    B = set([])
    Both = set([])
    for x in X:
        if a-x in X1 and b-x  not in X1:
            A.add(x)
            A.add(a-x)
        elif a-x not in X1 and b-x in X1:
            B.add(x)
            B.add(b-x)
        elif a-x not in X1 and b-x not in X1:
            return 'NO'
        else:
            Both.add(x)
    start = A.copy()
    while len(start) > 0:
        next_s = set([])
        for x in start:
            if b-x in Both:
                Both.remove(b-x)
                next_s.add(b-x)
                if a-b+x in Both:
                    Both.remove(a-b+x)
                    A.add(a-b+x)
                    next_s.add(a-b+x)
                A.add(b-x)
            if a-x in Both:
                Both.remove(a-x)
                next_s.add(a-x)
                A.add(a-x)
            elif a-x in B or a-x not in A:
                return 'NO'
        start = next_s
    start = B.copy()
    while len(start) > 0:
        next_s = set([])
        for x in start:
            if a-x in Both:
                Both.remove(a-x)
                next_s.add(a-x)
                if b-a+x in Both:
                    Both.remove(b-a+x)
                    B.add(b-a+x)
                    next_s.add(b-a+x)
                B.add(a-x)
            if b-x in Both:
                Both.remove(b-x)
                next_s.add(b-x)
                B.add(b-x)
            elif b-x in A or b-x not in B:
                return 'NO'
        start = next_s
    answer = []
    for x in X:
        if x in A:
            answer.append(0)
        else:
            answer.append(1)
    return answer

n, a, b = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]
answer = process(X, a, b)
if answer=='NO':
    print('NO')
else:
    print('YES')
    print(' '.join(map(str, answer)))
        
                
    
            