def main(n):
    # Deterministic data generation based on n
    # l[i]: number of greater elements before i
    # r[i]: number of greater elements after i
    # Use ans as a simple non-increasing sequence to keep constraints consistent
    ans_true = [n - i for i in range(n)]
    l = []
    r = []
    for i in range(n):
        ci = ans_true[i]
        left_greater = 0
        for j in range(i):
            if ans_true[j] > ci:
                left_greater += 1
        right_greater = 0
        for j in range(i + 1, n):
            if ans_true[j] > ci:
                right_greater += 1
        l.append(left_greater)
        r.append(right_greater)

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
    for i in ans:
        # print(i, end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)