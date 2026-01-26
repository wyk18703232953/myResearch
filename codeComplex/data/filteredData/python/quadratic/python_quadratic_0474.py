def main(n):
    if n <= 0:
        return

    # Deterministic generation of l and r based on n
    # l[i]: number of greater elements on the left of position i
    # r[i]: number of greater elements on the right of position i
    ans_true = [n - i for i in range(1, n + 1)]
    l = []
    r = []
    for i in range(n):
        li = 0
        for j in range(i):
            if ans_true[j] > ans_true[i]:
                li += 1
        l.append(li)
        ri = 0
        for j in range(i + 1, n):
            if ans_true[j] > ans_true[i]:
                ri += 1
        r.append(ri)

    ans = [1 for _ in range(n)]

    s = [l[i] + r[i] for i in range(n)]
    order = [i for i in range(n)]

    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if s[m] < s[j]:
                m = j
        t = s[i]
        s[i] = s[m]
        s[m] = t
        t = order[i]
        order[i] = order[m]
        order[m] = t

    cur = 1
    for i in range(1, n):
        if s[i - 1] > s[i]:
            cur += 1
        ans[order[i]] = cur

    for i in range(n):
        k = 0
        for j in range(i):
            if ans[j] > ans[i]:
                k += 1
        if l[i] != k:
            # print('NO')
            pass
            return
        k = 0
        for j in range(i + 1, n):
            if ans[j] > ans[i]:
                k += 1
        if r[i] != k:
            # print('NO')
            pass
            return

    # print('YES')
    pass
    for x in ans:
        # print(x, end=' ')
        pass
if __name__ == "__main__":
    main(10)