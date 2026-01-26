def isValid(arr, l, r, x):
    return l <= sum(arr) <= r and max(arr) - min(arr) >= x


def main(n):
    # n is the number of elements in the array
    if n <= 0:
        print(0)
        return

    # Deterministic parameter generation
    l = n  # minimal sum threshold
    r = n * (n + 1) // 2  # maximal possible sum of arr if arr[i] = i+1
    x = max(1, n // 3)  # minimal difference between max and min

    # Deterministic array generation: arr[i] = i + 1
    arr = [i + 1 for i in range(n)]

    valid = 0
    for mask in range(1, 1 << n):
        temp = []
        for j in range(n):
            if (mask >> j) & 1:
                temp.append(arr[j])
        if isValid(temp, l, r, x):
            valid += 1
    print(valid)


if __name__ == "__main__":
    main(5)