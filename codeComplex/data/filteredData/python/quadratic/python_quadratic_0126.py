def main(n):
    # n: number of "types"
    # We will generate m = n * 3 events deterministically
    m = n * 3
    # Generate li as a repeating pattern 1..n, truncated to length m
    li = [i % n + 1 for i in range(m)]

    dic = {}
    c = 0
    for i in range(n):
        dic.setdefault(i + 1, 0)
    for i in li:
        if 0 not in dic.values():
            c = c + 1
            for j in range(1, n + 1):
                dic[j] = dic[j] - 1
        dic[i] = dic[i] + 1
    if 0 not in dic.values():
        c = c + 1
    # print(c)
    pass
if __name__ == "__main__":
    main(10)