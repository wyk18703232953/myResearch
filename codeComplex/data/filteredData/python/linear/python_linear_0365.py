def main(n):
    # Interpret n as the number of elements in c and a, and also as m
    # Generate deterministic data
    # c: strictly increasing sequence starting from 1
    c = [i + 1 for i in range(n)]
    # a: every element is i//2 + 1 (non-decreasing sequence)
    a = [i // 2 + 1 for i in range(n)]
    m = n

    j, res = 0, 0
    for i in range(n):
        if j < m:
            if c[i] <= a[j]:
                j += 1
                res += 1
    # print(res)
    pass
if __name__ == "__main__":
    main(10)