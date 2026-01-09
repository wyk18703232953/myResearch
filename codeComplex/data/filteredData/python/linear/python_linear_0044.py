def main(n):
    # Deterministic data generation
    # Interpret n as array length; choose k as a small function of n
    if n <= 0:
        # print(-1, -1)
        pass
        return
    k = max(1, min(10, n // 3 + 1))
    a = [(i * 2 + 3) % (k + 3) + 1 for i in range(n)]

    # Original algorithm
    q = {0}
    e = 0
    l = []
    for i in range(n):
        if a[i] not in q:
            e += 1
            q.add(a[i])
        if e == k:
            e = 0
            q = {0}
            l += [i]
    w = 10 ** 5
    t = 0
    for i in l:
        e = 0
        q = {0}
        for j in range(i, -1, -1):
            if a[j] not in q:
                e += 1
                q.add(a[j])
            if e == k:
                if w > len(q):
                    w = j + 1
                    t = i + 1
                break
    if len(set(a)) >= k:
        # print(w, t)
        pass

    else:
        # print(-1, -1)
        pass
if __name__ == "__main__":
    main(1000)