def main(n):
    from collections import defaultdict

    # Deterministically generate input:
    # n: length of array
    # tar: a value that appears multiple times but not trivially
    # a: constructed using modular and arithmetic patterns
    if n <= 0:
        # print(0)
        pass
        return

    tar = (n // 3) + 1
    a = [(i * 2 + (i // 3)) % (n // 2 + 3) for i in range(n)]

    # Ensure tar appears at least once deterministically
    if n >= 1:
        a[0] = tar
    if n >= 3:
        a[n // 2] = tar
    if n >= 5:
        a[-1] = tar

    d = defaultdict(lambda: [])
    count = 0
    for i in range(n):
        d[a[i]].append(i)
        if a[i] == tar:
            count += 1

    presum = [1 if a[0] == tar else 0]
    for e in a[1:]:
        if e == tar:
            presum.append(presum[-1] + 1)

        else:
            presum.append(presum[-1])

    final = 0
    for k, v in d.items():
        if k == tar:
            continue

        t = 1
        tt = 1
        for i in range(1, len(v)):
            ind = v[i]
            preind = v[i - 1]

            t -= presum[ind] - presum[preind]
            t = max(t, 0)
            t += 1
            tt = max(tt, t)

        final = max(final, tt)

    # print(final + count)
    pass
if __name__ == "__main__":
    main(10)