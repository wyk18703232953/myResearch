def main(n):
    # Interpret n as the length of the list l
    if n <= 0:
        print(0)
        return

    # Deterministic generation of parameters and list
    least = n
    highest = 3 * n
    x = max(1, n // 3)

    # Deterministic list of length n
    l = [i % 10 + i // 2 for i in range(1, n + 1)]

    cnt = 0
    for size in range(2, n + 1):
        combo_list = [list(c) for c in combinations(l, size)]
        for comb in combo_list:
            comb.sort()
            total = sum(comb)
            if least <= total <= highest and comb[-1] - comb[0] >= x:
                cnt += 1
    print(cnt)


from itertools import combinations

if __name__ == "__main__":
    main(10)