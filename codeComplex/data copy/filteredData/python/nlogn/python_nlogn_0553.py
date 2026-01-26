def main(n):
    l = [-1 for _ in range(n + 1)]
    # deterministic generation of ll: a permutation-like cyclic shift
    ll = [(i % n) + 1 for i in range(1, n + 1)]
    for i in range(n):
        j = ll[i]
        l[j] = i
    res = ["." for _ in range(n + 1)]
    res[n] = "B"
    for i in range(n - 1, 0, -1):
        toadd = "B"
        pos = l[i] % i
        while pos < n:
            j = ll[pos]
            if j <= i:
                pos += i
                continue
            if abs(l[i] - l[j]) % i == 0 and res[j] == "B":
                toadd = "A"
                break
            pos += i
        res[i] = toadd
    output = []
    for i in ll:
        output.append(res[i])
    # print("".join(output))
    pass
if __name__ == "__main__":
    main(10)