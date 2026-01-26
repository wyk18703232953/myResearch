def main(n):
    # Deterministic generation of k and p based on n
    # n controls the length of p
    if n <= 0:
        return
    k = max(1, n // 3)
    p = [((i * 7) % (2 * n)) for i in range(n)]

    mp = {}
    res = []

    for pi in p:
        if mp.get(pi) is None:
            key = pi
            for j in range(pi, pi - k, -1):
                if j < 0:
                    break
                if mp.get(j) is None:
                    key = j

                else:
                    if mp[j] >= pi - k + 1:
                        key = mp[j]
                    break
            for j in range(pi, key - 1, -1):
                if mp.get(j):
                    break
                mp[j] = key
        res.append(mp[pi])

    # print(*res, sep=" ")
    pass
if __name__ == "__main__":
    main(10)