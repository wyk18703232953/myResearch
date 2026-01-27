def main(n):
    # Interpret n as the magnitude of the input values.
    # Generate a single test case deterministically from n.
    h = n
    b = n * 2
    x = n + 1
    y = n + 2
    z = n + 3
    result = max(0, 2 * x + y - h) + max(0, 3 * z + y - b)
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)