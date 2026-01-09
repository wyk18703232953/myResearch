def main(n):
    # Generate deterministic input based on n
    # Interpret n as the number of distinct elements required in set a
    # Generate a as first n integers starting from 0
    x = n // 2 + 1  # deterministic choice of x depending on n
    a = set(range(n))

    if len(a) < n:
        # print(0)
        pass

    else:
        d = set()
        p = 0
        for i in a:
            val = i & x
            d.add(val)
            if val != i and val in a:
                # print(1)
                pass
                p = 1
                break
        if len(d) < n and p == 0:
            # print(2)
            pass
        elif p != 1:
            # print(-1)
            pass
if __name__ == "__main__":
    main(10)