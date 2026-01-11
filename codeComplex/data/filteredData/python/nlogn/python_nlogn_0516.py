def main(n):
    from collections import defaultdict as dd

    # Interpret n as number of test cases; each test case size = i+2
    T = n
    results = []
    for t in range(1, T + 1):
        size = t + 2
        l = [(i % (size // 2 + 1)) + 1 for i in range(size)]
        l1 = dd(int)
        a = 0
        for j in l:
            l1[j] += 1
            if l1[j] == 4:
                a = j
        if a:
            results.append((a, a, a, a))

        else:
            c = 0
            x = 0
            l2 = []
            for j in l1:
                if l1[j] >= 2:
                    l2.append(j)
            l2.sort()
            a = 0
            b = 0
            for j in l2:
                c += 1
                if c == 1:
                    a = j
                elif c == 2:
                    b = j

                else:
                    if x / j + j / x < a / b + b / a:
                        a, b = x, j
                x = j
            results.append((a, a, b, b))

    # Output to keep same observable behavior as original (for analysis)
    for quad in results:
        # print(*quad)
        pass
if __name__ == "__main__":
    main(5)