def main(n):
    # n is the number of operations m
    m = n
    values = []
    idx = []
    for i in range(m):
        # deterministically generate x from i and n
        x = (i * 2 + 1) ^ n
        ans = 0
        for j, xx in enumerate(values):
            if (xx ^ x) < x:
                x ^= xx
                ans ^= idx[j]
        if x == 0:
            anss = []
            tmp = ans
            for j in range(i):
                if (tmp & 1) != 0:
                    anss.append(j)
                tmp >>= 1
            if anss:
                print(len(anss), *anss)
            else:
                print(0)
        else:
            print(0)
            values.append(x)
            idx.append(ans ^ (2 ** i))


if __name__ == "__main__":
    main(10)