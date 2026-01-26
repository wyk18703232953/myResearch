def main(n):
    # n controls total length of x and t (n + m in original).
    # For simplicity, we let total_len = max(2, n) and choose m = total_len // 2.
    total_len = max(2, n)
    m = total_len // 2
    n_local = total_len - m

    # Deterministically construct x and t based on total_len, n_local, m.
    # x: an integer list of length total_len
    x = [(i * 2 + 3) % (total_len + 5) for i in range(total_len)]

    # t: a binary list with exactly n_local zeros and m ones.
    # Place zeros at even indices first, then fill remaining needed zeros.
    t = [1] * total_len
    zeros_to_place = n_local
    # place zeros on even indices
    for i in range(0, total_len, 2):
        if zeros_to_place > 0:
            t[i] = 0
            zeros_to_place -= 1

        else:
            break
    # if still need zeros, place from the beginning on odd indices
    if zeros_to_place > 0:
        for i in range(1, total_len, 2):
            if t[i] == 1 and zeros_to_place > 0:
                t[i] = 0
                zeros_to_place -= 1
            if zeros_to_place == 0:
                break

    arr = []
    pep = {}
    for i in range(n_local + m):
        if t[i] == 0:
            arr.append(i)
            pep[x[i]] = 0

        else:
            for j in arr:
                pep[x[j]] = i
            arr = []
    for i in range(n_local + m - 1, -1, -1):
        if t[i] == 0:
            arr.append(i)

        else:
            for j in arr:
                if abs(x[j] - x[i]) <= abs(x[pep[x[j]]] - x[j]):
                    pep[x[j]] = i
            arr = []
    ans = []
    for i in range(n_local + m):
        if t[i]:
            ans.append(1)

        else:
            ans.append(0)
    for i in pep:
        ans[pep[i]] += 1
    for i in ans:
        if i:
            # print(i - 1, end=' ')
            pass
    # print()
    pass
if __name__ == "__main__":
    # Example deterministic calls for experimentation
    main(10)
    main(100)