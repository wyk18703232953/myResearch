from math import ceil, log

def main(n):
    # Deterministically generate input data of size n
    # Original program structure:
    # n: length of list a
    # a: list of n integers
    #
    # Here we construct a with some variety but fully deterministic.
    # Example pattern: a[i] = (i % 7) + (i // 3) + 1
    a = [(i % 7) + (i // 3) + 1 for i in range(n)]

    d = {}
    m = -1
    mm = 10**10

    for v in a:
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
        if v > m:
            m = v
        if v < mm:
            mm = v

    ans = 0

    for v in a:
        exponent = ceil(log(v, 2))
        power = 2 ** exponent
        find = 0
        while power - v >= 0:
            if power - v > mm and power - v > m:
                break

            element = power - v
            if element in d and element == v and d[element] > 1:
                find = 1
                break
            elif element in d and element != v:
                find = 1
                break
            power = power * 2
        if find == 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(1000)