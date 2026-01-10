def main(n):
    # Interpret n as the size of array a
    # Generate deterministic test data:
    # m is chosen as n // 2, a is a descending list of n integers
    m = n // 2
    a = [n * 3 - i for i in range(n)][::-1]  # original code uses reversed input; here we build directly

    cur, ans = 2, -1

    for i in range(n - 2):
        cur = max(cur, i + 2)
        for j in range(cur, n):
            if a[i] - a[j] > m:
                break

            cur += 1
            v = (a[i] - a[j - 1]) / (a[i] - a[j])
            if v > ans:
                ans = v

    print(ans)


if __name__ == "__main__":
    main(1000)