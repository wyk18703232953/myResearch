def main(n):
    from collections import defaultdict

    # Deterministic construction of input:
    # Original program expects:
    # n
    # l[1..n] as a permutation-like or integer list.
    # Here we construct l as [0, 1, 2, ..., n] so l[i] = i.
    l = [0] + [i for i in range(1, n + 1)]

    ans = ['A', 'B']
    x = defaultdict(int)
    table = [-1] * (n + 1)

    for i in range(1, n + 1):
        x[l[i]] = i

    table[x[n]] = 1
    for i in range(n - 1, 0, -1):
        if x[i] - i > 0:
            for j in range(x[i], 0, -i):
                if l[j] > i:
                    if table[j] == 1:
                        table[x[i]] = 0
                        break
        if n - i > 0 and table[x[i]] == -1:
            for j in range(x[i], n + 1, i):
                if l[j] > i:
                    if table[j] == 1:
                        table[x[i]] = 0
                        break

        if table[x[i]] == -1:
            table[x[i]] = 1

    for i in table[1:]:
        # print(ans[i], end='')
        pass
if __name__ == "__main__":
    main(10)