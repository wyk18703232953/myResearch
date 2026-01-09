def main(n):
    # Interpret n as the length of array a; set m and k as functions of n
    # Ensure m is at least 1 and at most n
    m = max(1, min(n, n // 2 if n > 1 else 1))
    k = n // 3 + 1

    # Deterministic construction of array a of length n
    # Example pattern: a[j] = (j * 7) % 11 - 5  (values in [-5,5])
    a = [(j * 7) % 11 - 5 for j in range(n)]

    values = []

    for j in range(n):
        result = a[j]
        sum1 = 0
        for i in range(m):
            if j - i >= 0:
                sum1 = sum1 + a[j - i]
                if sum1 > result:
                    result = sum1

            else:
                continue
        if j - m >= 0:
            result = max(result, sum1 + values[j - m])
        values.append(max(0, result - k))
    if values:
        # print(max(values))
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    main(1000)