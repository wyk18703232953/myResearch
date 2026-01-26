def main(n):
    # Generate deterministic input array xs of length 14 based on n
    xs = [((i + 1) * (n + 1)) % 1000 for i in range(14)]

    res = 0
    for i in range(14):
        newxs = xs[:]
        newxs[i] = 0
        base_add = xs[i] // 14
        rem = xs[i] % 14

        for j in range(14):
            newxs[j] += base_add

        for j in range(rem):
            newxs[(i + 1 + j) % 14] += 1

        even_sum = 0
        for val in newxs:
            if val % 2 == 0:
                even_sum += val

        if even_sum > res:
            res = even_sum

    # print(res)
    pass
if __name__ == "__main__":
    main(10)