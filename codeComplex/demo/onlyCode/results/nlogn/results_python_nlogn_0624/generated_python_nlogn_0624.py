def push(d, u, v):
    if u not in d:
        d[u] = []
    if v not in d:
        d[v] = []
    d[u].append(v)
    d[v].append(u)

def push_v(d, u, val):
    if u not in d:
        d[u] = 0
    d[u] += val

def main(n):
    if n < 3:
        return 'NO'
    k = 2
    g = {}
    for i in range(2, n + 1):
        push(g, 1, i)
    deg1 = []
    used = [0] * (n + 1)
    for u in g:
        if len(g[u]) == 1:
            used[u] = 1
            deg1.append(u)
    flg = True
    while k > 0:
        if k >= 1 and len(deg1) < 3:
            flg = False
            break
        cnt = {}
        for u in deg1:
            for v in g[u]:
                if used[v] == 0:
                    push_v(cnt, v, 1)
        for v in deg1:
            used[v] = 1
        deg1 = []
        for v, val in cnt.items():
            if val < 3:
                flg = False
                break
            deg1.append(v)
        if flg == False:
            break
        k -= 1
    if flg == True and len(deg1) > 1:
        flg = False
    return 'YES' if flg else 'NO'

if __name__ == "__main__":
    print(main(10))