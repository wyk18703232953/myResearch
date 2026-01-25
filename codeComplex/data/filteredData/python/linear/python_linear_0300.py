def main(n):
    # deterministic input generation: a is a list of length n
    # using simple arithmetic pattern based on index
    a = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]

    b = [0] * n
    for i in range(n):
        if (i + 1 > a[i]):
            b[i] = i + 1
        else:
            q = (a[i] - (i + 1) + n) // n
            b[i] = i + 1 + q * n
    result = b.index(min(b)) + 1
    print(result)
    return result


if __name__ == "__main__":
    # example call; you can adjust n for different scales
    main(10)