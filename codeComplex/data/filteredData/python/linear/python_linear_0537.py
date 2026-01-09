def main(n):
    # Generate deterministic test data of length n
    # Example pattern: a[i] = i - n//2, which gives both negative and positive values
    a = [i - n // 2 for i in range(n)]

    if n == 1:
        # print(a[0])
        pass

    else:
        prod_minus = False
        for i in range(n - 1):
            if a[i] * a[i + 1] <= 0:
                prod_minus = True
                break
        Min_abs = float("inf")
        Sum = 0
        for num in a:
            Sum += abs(num)
            if abs(num) < Min_abs:
                Min_abs = abs(num)

        if prod_minus:
            # print(Sum)
            pass

        else:
            # print(Sum - 2 * Min_abs)
            pass
if __name__ == "__main__":
    main(10)