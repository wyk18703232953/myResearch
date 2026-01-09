def main(n):
    # Interpret n as both the original n and the number of rows m
    m = n

    # Deterministic generation of arr with shape (m, 2)
    # arr[i] = [a, b] where:
    #   a = i
    #   b = (-1)**i * (i % 5 + 1)  -> alternating sign, bounded magnitude
    arr = []
    for i in range(m):
        a = i
        b = (1 if i % 2 == 0 else -1) * (i % 5 + 1)
        arr.append([a, b])

    count = 0
    for i in range(m):
        count += arr[i][0] * n
        if n % 2 == 1 and arr[i][1] < 0:
            count += (n // 2) * (n // 2 + 1) * arr[i][1]
        if n % 2 == 1 and arr[i][1] > 0:
            count += n * (n - 1) * arr[i][1] // 2
        if n % 2 == 0 and arr[i][1] < 0:
            count += (n // 2) * (n // 2 - 1) * arr[i][1]
            count += (n // 2) * arr[i][1]
        if n % 2 == 0 and arr[i][1] > 0:
            count += n * (n - 1) * arr[i][1] // 2

    # print(count / n if n != 0 else 0)
    pass
if __name__ == "__main__":
    main(10)