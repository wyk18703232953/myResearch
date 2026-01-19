def main(n):
    # Interpret n as the length of the array
    if n <= 0:
        return 0

    # Deterministically generate parameters and array
    l = n
    r = 3 * n
    x = max(1, n // 3)

    arr = [i + 1 for i in range(n)]

    ans = 0
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset.append(arr[j])
        if len(subset) > 1:
            mx = max(subset)
            mn = min(subset)
            sm = sum(subset)
            if l <= sm <= r and mx - mn >= x:
                ans += 1
    return ans


if __name__ == "__main__":
    # Example call for demonstration
    result = main(5)
    print(result)