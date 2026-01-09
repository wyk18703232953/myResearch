def main(n):
    # Interpret n as the length of the sequence ps
    # Generate deterministic ps values in [0, 255]
    k = max(1, n // 3)  # deterministic relation between n and k
    ps = [(i * 7) % 256 for i in range(n)]

    mapping = [-1 for _ in range(256)]

    res = []
    for p in ps:
        if mapping[p] == -1:
            j = p - k + 1
            while j < 0 or (mapping[j] != -1 and mapping[j] + k <= p):
                j += 1
            for i in range(j, p + 1):
                mapping[i] = j
        res.append(mapping[p])

    # print("n =", n, "k =", k)
    pass
    # print(" ".join(map(str, res)))
    pass
if __name__ == "__main__":
    main(10)