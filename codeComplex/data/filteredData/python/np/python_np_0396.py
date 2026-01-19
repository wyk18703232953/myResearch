import sys
from collections import defaultdict as dd

def main(n):
    # n controls number of rows; keep columns small and fixed
    if n <= 0:
        return
    m = 5
    # deterministic generation of matrix l1 with values in [0, 10^9]
    l1 = []
    for i in range(n):
        row = []
        for j in range(m):
            val = (i * (j + 3) * 1234567 + (i + j) * 890123) % (10**9 + 7)
            val = val % (10**9)
            row.append(val)
        l1.append(row)

    l = 0
    h = 10**9
    c = 2**m - 1
    x, y = 1, 2
    while l <= h:
        mid = (l + h) // 2
        d = dd(int)
        d1 = dd(int)
        for i in range(n):
            s_bits = []
            for j in range(m):
                if l1[i][j] >= mid:
                    s_bits.append("1")
                else:
                    s_bits.append("0")
            s = int("".join(s_bits), 2)
            d[s] += 1
            d1[s] = i + 1
        f = 0
        for i_key in d:
            for j_key in d:
                if i_key | j_key == c:
                    f = 1
                    x = d1[i_key]
                    y = d1[j_key]
                    break
            if f:
                break
        if f:
            if l == h:
                break
            l = mid + 1
        else:
            if l == h:
                break
            h = mid
    print(x, y)


if __name__ == "__main__":
    # example deterministic call; change n to vary input size
    main(1000)