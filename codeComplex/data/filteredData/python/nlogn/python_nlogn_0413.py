from collections import defaultdict

def main(n):
    ans = defaultdict(int)

    # Deterministic generation of n intervals
    # Interval i: [i, i + (i % 5) + 1]
    beg = [0] * n
    end = [0] * n
    for i in range(n):
        a = i
        length = (i % 5) + 1
        b = a + length
        beg[i] = a
        end[i] = b + 1

    beg.sort()
    end.sort()

    pa, pb = 0, 0
    cur = 0
    lst = -1

    while pb < n:
        pos = end[pb]
        if pa < n:
            pos = min(pos, beg[pa])

        ans[cur] += pos - lst

        ad = 0
        mn = 0
        while pa < n and beg[pa] == pos:
            ad += 1
            pa += 1
        while pb < n and end[pb] == pos:
            pb += 1
            mn -= 1

        lst = pos
        cur += ad + mn

    for i in range(1, n + 1):
        print(ans[i], end=' ')
    print()


if __name__ == "__main__":
    main(10)