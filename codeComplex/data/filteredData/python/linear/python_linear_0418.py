def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministically generate x based on n
    x = (n * 37) ^ 123456

    # Deterministically generate list b of length n
    # Use a simple arithmetic pattern with bit operations
    b = [((i * 17) ^ (i // 2) ^ n) & 0xffff for i in range(1, n + 1)]

    d = {}
    flag = 0
    for i in b:
        if d.get(i):
            flag = 1
            break
        else:
            d[i] = 1
    if flag:
        print(0)
    else:
        flag = 0
        c = set()
        for i in b:
            a = i & x
            c.add(a)
            if d.get(a) and a != i:
                flag = 1
                break
        if flag:
            print(1)
        elif len(c) < n and flag == 0:
            print(2)
        else:
            print(-1)


if __name__ == "__main__":
    # Example deterministic call
    main(10)