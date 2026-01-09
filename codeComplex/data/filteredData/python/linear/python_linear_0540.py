def main(n):
    # Generate deterministic input array a of length n
    # Example pattern: a[i] = (-1)**i * (i % 7 + 1)
    a = [((-1) ** i) * (i % 7 + 1) for i in range(n)]

    if n == 0:
        # Define behavior for n = 0 (not present in original problem but needed for completeness)
        # print(0)
        pass
        return

    if n == 1:
        # print(a[0])
        pass

    else:
        sm = 0
        havePositive = False
        haveNegative = False

        for c in a:
            if c == 0:
                haveNegative = True
                havePositive = True
            elif c > 0:
                havePositive = True
                sm += c

            else:
                haveNegative = True
                sm -= c

        if haveNegative and havePositive:
            # print(sm)
            pass

        else:
            for i in range(n):
                a[i] = abs(a[i])
            ans = sum(a)
            low = a[0]
            for c in a:
                low = min(low, c)
            # print(ans - 2 * low)
            pass
if __name__ == "__main__":
    main(10)