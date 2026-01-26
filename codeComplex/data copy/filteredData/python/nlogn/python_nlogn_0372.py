def main(n):
    # Interpret n as both the number of elements and the max element magnitude
    # Deterministic array generation: arr[i] = (i * 3) % (n // 2 + 1)
    if n <= 0:
        return 0

    k = n // 3  # deterministic choice for k based on n
    arr = [(i * 3) % (n // 2 + 1) for i in range(n)]

    arr.sort()
    f = arr[0]
    p = n
    i = 0
    count = 0
    while i < n:
        while i < n and arr[i] == f:
            i += 1
            count += 1
        if i < n and arr[i] <= f + k:
            p -= count
        if i < n:
            f = arr[i]
            count = 0
        continue

    return p


if __name__ == "__main__":
    # Example call for time complexity experiments
    result = main(10)
    # print(result)
    pass