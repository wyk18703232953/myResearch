def main(n):
    # Interpret n as the length of array a
    if n <= 0:
        return 0

    # Deterministic construction of k and a
    # k ranges from 1 to n
    k = max(1, n // 3)  # for scaling experiment; deterministic function of n

    # Construct a strictly increasing sequence to keep original logic meaningful
    # a[i] = i * 2 + (i // 2) ensures increasing and deterministic values
    a = [i * 2 + (i // 2) for i in range(n)]

    # Original core logic
    s = []
    for q in range(n - 1):
        s.append([a[q + 1] - a[q], q])
    s.sort(reverse=True)
    d = {q[1] for q in s[:max(0, k - 1)]}
    ans = 0
    q1 = a[0]
    for q in range(n - 1):
        if q in d:
            ans += a[q] - q1
            q1 = a[q + 1]
    result = ans + a[-1] - q1

    # For time complexity experiments one might just return the result
    return result


if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    # print(main(10))
    pass