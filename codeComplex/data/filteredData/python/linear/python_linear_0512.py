def main(n):
    # Generate deterministic test data based on n
    # a and b are lists of characters '0' and '1'
    a = [str((i // 2) % 2) for i in range(n)]
    b = [str((i // 3) % 2) for i in range(n)]

    ans = 0

    for i in range(n - 1):
        if a[i] == b[i]:
            continue
        if a[i + 1] == b[i + 1]:
            continue

        if a[i] == b[i + 1] and a[i + 1] == b[i]:
            a[i], a[i + 1] = a[i + 1], a[i]
            ans += 1

    for i in range(n):
        ans += a[i] != b[i]

    return ans


if __name__ == "__main__":
    # Example deterministic call for experimentation
    result = main(10)
    # print(result)
    pass