def main(n):
    if n <= 0:
        return 0
    # Deterministically generate input array of length n
    # Example pattern: arr[i] = (i * 3 + i // 2) % (n + 5)
    arr = [((i * 3 + i // 2) % (n + 5)) for i in range(n)]

    t = [0] * n
    cur = 0
    for i in range(n - 1, -1, -1):
        cur = max(cur - 1, 0, arr[i] + 1)
        t[i] = cur
    ans = 0
    for i in range(n):
        cur = max(cur, t[i])
        ans += cur
    for i in range(n):
        ans -= (arr[i] + 1)
    print(ans)
    return ans


if __name__ == "__main__":
    main(10)