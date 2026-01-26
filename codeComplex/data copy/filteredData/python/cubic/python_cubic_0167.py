def main(n):
    # Generate deterministic input array 'a' of length n
    # Example pattern: a[i] = (i % 3)
    a = [i % 3 for i in range(n)]

    grip = [[-1] * (n - i) for i in range(n)]
    grip[0] = a.copy()
    for level in range(1, n):
        for left in range(n - level):
            for split in range(level):
                pl = grip[level - split - 1][left]
                pr = grip[split][left + level - split]
                if pl == pr != -1:
                    grip[level][left] = pl + 1
    pref = [0] * (n + 1)
    for p in range(1, n + 1):
        x = n
        for j in range(p):
            l = pref[j]
            r = grip[p - j - 1][j]
            if r == -1:
                r = p - j

            else:
                r = 1
            x = min(x, l + r)
        pref[p] = x
    return pref[-1]


if __name__ == "__main__":
    # Example deterministic call; you can change n as needed for experiments
    result = main(10)
    # print(result)
    pass