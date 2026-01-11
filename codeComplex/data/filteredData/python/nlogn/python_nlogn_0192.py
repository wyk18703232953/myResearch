def main(n):
    # Deterministically generate input array of size n
    # Example pattern: b[i] = (i % 5) - 2, so values in [-2, 2]
    b = [(i % 5) - 2 for i in range(n)]

    cnt = {}
    ans = 0

    for i in range(n):
        ans += b[i] * i + (-b[i]) * (n - i - 1)

    for i in range(n):
        if (b[i] - 1) in cnt:
            ans -= cnt[b[i] - 1]
        if (b[i] + 1) in cnt:
            ans += cnt[b[i] + 1]
        if b[i] in cnt:
            cnt[b[i]] += 1

        else:
            cnt[b[i]] = 1

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)