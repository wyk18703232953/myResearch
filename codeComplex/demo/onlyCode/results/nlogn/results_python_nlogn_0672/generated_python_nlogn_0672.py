from collections import deque
import random

def main(n):
    N = n
    M = n * 2
    table = []
    for _ in range(M):
        s = random.randrange(N)
        t = random.randrange(N)
        c = random.randint(0, 10**9)
        table.append((s, t, c))

    def check(k):
        Lin = [0] * N
        edge = [[] for _ in range(N)]
        for s, t, c in table:
            if c > k:
                Lin[t] += 1
                edge[s].append(t)
        Haco = deque()
        ans = []
        for i in range(N):
            if Lin[i] == 0:
                ans.append(i)
                Haco.append(i)
        while Haco:
            x = Haco.pop()
            for y in edge[x]:
                Lin[y] -= 1
                if Lin[y] == 0:
                    ans.append(y)
                    Haco.append(y)
        return ans

    ma = 10**9 + 7
    mi = -1
    while ma - mi > 1:
        mid = (ma + mi) // 2
        if len(check(mid)) == N:
            ma = mid
        else:
            mi = mid
    ans = check(ma)
    dd = {}
    for i in range(N):
        dd[ans[i]] = i
    num = 0
    answer = []
    for i in range(M):
        s, t, c = table[i]
        if dd[s] > dd[t] and c <= ma:
            answer.append(i + 1)
            num += 1
    print(ma, num)
    if answer:
        print(' '.join(map(str, answer)))
    else:
        print()

if __name__ == "__main__":
    main(5)