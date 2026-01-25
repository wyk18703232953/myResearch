def main(n):
    # n is the size of the input: length of arrays a and t, and also k (clamped to at least 1)
    if n <= 0:
        return 0

    k = max(1, n // 2)

    # Deterministic construction of a and t based on n
    # a: increasing positive integers starting from 1
    a = [i + 1 for i in range(n)]
    # t: periodic pattern of 0 and 1 depending on index
    t = [(i // 2) % 2 for i in range(n)]

    p = [0] * (n + 1)
    now = 0
    for i in range(0, n):
        if t[i] == 1:
            now += a[i]
        p[i + 1] = p[i]
        if t[i] == 0:
            p[i + 1] += a[i]
    s = 0
    for i in range(n - k + 1):
        s = max(s, p[i + k] - p[i])
    result = now + s
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    main(10)
    main(100)