def main(n):
    m = n
    values = []
    idx = []
    for i in range(m):
        x = i + 1
        ans = 0
        for xx, ii in zip(values, idx):
            if (xx ^ x) < x:
                x ^= xx
                ans ^= ii
        if x == 0:
            anss = []
            tmp = ans
            for j in range(i):
                if (tmp & 1) == 1:
                    anss.append(j)
                tmp >>= 1
            print(len(anss), *anss)
        else:
            print(0)
            values.append(x)
            idx.append(ans ^ (1 << i))


if __name__ == "__main__":
    main(10)