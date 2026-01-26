def main(n):
    from collections import defaultdict

    # ensure n >= 1
    if n <= 0:
        return

    # deterministically generate a permutation l[1..n]
    # simple pattern: cyclic shift by 1
    l = [0] + [((i % n) + 1) for i in range(1, n + 1)]

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

    result = []
    for i in table[1:]:
        result.append(ans[i])
    output = ''.join(result)
    # print(output)
    pass
    return output


if __name__ == "__main__":
    # example deterministic call
    main(10)