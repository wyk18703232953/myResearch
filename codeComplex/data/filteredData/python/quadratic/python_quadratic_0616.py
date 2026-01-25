def main(n):
    # Interpret n as both the array length and parameter m
    if n <= 0:
        print(0)
        return

    # Deterministically generate n, m, k and array a based on input scale n
    N = n
    M = n
    K = n // 2 + 1

    a = [(i * 2 + 1) % (n + 3) for i in range(N)]

    values = []
    for j in range(N):
        result = a[j]
        sum1 = 0
        for i in range(M):
            if j - i >= 0:
                sum1 = sum1 + a[j - i]
                if sum1 > result:
                    result = sum1
            else:
                continue
        if j - M >= 0:
            result = max(result, sum1 + values[j - M])
        values.append(max(0, result - K))
    print(max(values) if values else 0)


if __name__ == "__main__":
    main(10)