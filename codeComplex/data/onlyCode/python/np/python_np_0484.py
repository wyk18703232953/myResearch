def main():
    import sys
    import collections
    input = sys.stdin.readline
    n, m, K = map(int, input().split())

    A = [input().rstrip() for i in range(n)]

    B = [list(input().rstrip().split()) for i in range(m)]

    alpha = 'abcｄ'

    D = dict()
    for i, x in enumerate(A):
        D[x] = i

    G = [set() for i in range(n)]
    X = [set() for i in range(n)]

    for i in range(m):
        a, b = B[i]
        b = int(b)
        flag = False
        for j in range(2**K):
            x = []
            for k in range(K):
                if (j >> k) % 2 == 1:
                    x.append('_')
                else:
                    x.append(a[k])
            x = ''.join(x)
            if x in D:
                if D[x] == b-1:
                    flag = True
                    continue
                else:
                    G[b-1].add(D[x])
                    X[D[x]].add(b-1)
        if flag:
            continue
        else:
            print("NO")
            exit(0)
    X = [len(X[i]) for i in range(n)]
    ANS = []
    s = set()
    q = collections.deque()
    for i in range(n):
        if X[i] == 0:
            q.append(i)
            s.add(i)
    # print(G)
    # print(X)
    while(q):
        if len(ANS) == n:
            print("NO")
            exit(0)
        x = q.popleft()
        ANS.append(x+1)
        for y in G[x]:
            if X[y] == 0:
                continue
            else:
                X[y] -= 1
                if X[y] == 0:
                    q.append(y)
    if len(ANS) == n:
        print("YES")
        print(*ANS)
    else:
        print("NO")


main()
