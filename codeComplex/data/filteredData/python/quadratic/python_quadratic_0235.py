def main(n):
    # Generate deterministic test data based on n
    # s: sequence of length n
    # a: sequence of length n
    s = [i % 10 for i in range(n)]
    a = [i % 7 + 1 for i in range(n)]

    t = 3 * 10**9
    q = [0] * n
    for i in range(n - 1, -1, -1):
        u = 10**8
        for j in range(i - 1, -1, -1):
            if s[i] > s[j]:
                u = min(u, a[j])
        q[i] = u
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] < s[j]:
                t = min(t, a[i] + a[j] + q[i])
    result = t if t <= sum(a) else -1
    return result


if __name__ == "__main__":
    # Example call for time complexity experiments
    n = 1000
    # print(main(n))
    pass