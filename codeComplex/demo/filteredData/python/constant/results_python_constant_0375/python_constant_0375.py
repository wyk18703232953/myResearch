def main(n):
    # Generate deterministic inputs a, b, c based on n
    a = n
    b = 2 * n
    c = n // 2 + 1

    u = a + b - c
    if a < c or b < c:
        # print(-1)
        pass

    else:
        if n - u >= 1:
            # print(n - u)
            pass

        else:
            # print(-1)
            pass
if __name__ == "__main__":
    main(10)