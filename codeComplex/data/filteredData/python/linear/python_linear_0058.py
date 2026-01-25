def main(n):
    # Ensure n is at least 1 to avoid empty strings
    if n <= 0:
        n = 1

    # Deterministic construction of s and t of length n
    # s: repeating pattern "ab"
    # t: repeating pattern "ba"
    base_s = "ab"
    base_t = "ba"
    s = "".join(base_s[i % 2] for i in range(n))
    t = "".join(base_t[i % 2] for i in range(n))

    dif = {}
    hem = 0
    for i in range(n):
        if s[i] != t[i]:
            dif[i] = [s[i], t[i]]
            hem += 1

    change = []
    probed = []
    k = 0
    for i in dif.keys():
        if dif[i] in probed:
            continue
        probed.append(dif[i])
        k += 1
        for j in list(dif.keys())[k:]:
            if dif[i] == dif[j][::-1]:
                print(hem - 2)
                print(i + 1, j + 1)
                return
            if not change and (dif[i][0] == dif[j][1] or dif[j][0] == dif[i][1]):
                change = [i, j]

    if change:
        print(hem - 1)
        print(change[0] + 1, change[1] + 1)
    else:
        print(hem)
        print('-1 -1')


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)