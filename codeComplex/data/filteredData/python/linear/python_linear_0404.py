def main(n):
    # Generate deterministic input based on n
    # Original program expects:
    # line1: (ignored)
    # line2: m (integer)
    # line3 and line4: integers to be processed
    m = n if n > 1 else 2
    v = m
    # Generate a list of 2*n integers, avoiding 1 to prevent division by zero
    # If n is small, ensure at least some values
    length = max(2, 2 * n)
    arr = [i + 2 for i in range(length)]  # values: 2,3,4,...
    try:
        for a in arr:
            if a - 1 == 0:
                raise ZeroDivisionError
            v *= a / (a - 1)
    except ZeroDivisionError:
        v = m - 1
    # print(v - m)
    pass
if __name__ == "__main__":
    main(1000000010)
    print('ok')