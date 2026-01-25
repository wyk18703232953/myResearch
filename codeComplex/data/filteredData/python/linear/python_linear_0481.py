import math
from collections import defaultdict, deque

def main(n):
    # n: number of intervals
    t = max(2, n)

    # Deterministic interval generation
    # For i in [0, t-1], create [L_i, R_i] with L_i <= R_i
    tup = []
    for i in range(t):
        l = i
        r = i + (i % 5) + 1
        tup.append([l, r])

    tup.sort()
    l = tup[0][0]
    r = tup[0][1]
    prefix = [[l, r]]
    for i in range(1, t):
        if l > tup[i][1] or r < tup[i][0]:
            prefix.append([-1, -1])
            for j in range(i + 1, t):
                prefix.append([-1, -1])
            break

        l = max(l, tup[i][0])
        r = min(r, tup[i][1])
        prefix.append([l, r])

    l = tup[-1][0]
    r = tup[-1][1]
    suffix = []
    for i in range(t):
        suffix.append([-1, -1])
    suffix[-1][0] = l
    suffix[-1][1] = r
    for i in range(t - 2, -1, -1):
        if l > tup[i][1] or r < tup[i][0]:
            break

        l = max(l, tup[i][0])
        r = min(r, tup[i][1])
        suffix[i][0] = l
        suffix[i][1] = r

    ans = 0
    for i in range(t):
        if i == 0:
            if t > 1:
                ans = max(ans, abs(suffix[i + 1][0] - suffix[i + 1][1]))
            continue
        if i == t - 1:
            ans = max(ans, abs(prefix[i - 1][0] - prefix[i - 1][1]))
            continue
        prefix_l = prefix[i - 1][0]
        prefix_r = prefix[i - 1][1]
        suffix_l = suffix[i + 1][0]
        suffix_r = suffix[i + 1][1]
        l = max(prefix_l, suffix_l)
        r = min(prefix_r, suffix_r)
        ans = max(ans, max(0, r - l))
    print(ans)


if __name__ == "__main__":
    main(10)