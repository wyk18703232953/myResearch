def main(n):
    ans = {}
    # First batch size and second batch size are both n
    # Generate first batch of (a, b)
    # a: 1..n, b: i % 7 + i // 3 (deterministic but non-trivial)
    for i in range(1, n + 1):
        a = i
        b = (i % 7) + (i // 3)
        ans[a] = b

    # Second batch of (a, b)
    # a: (i % n) + 1 to ensure overlap, b: (i * 2) % 11 + i // 5
    for i in range(1, n + 1):
        a = (i % n) + 1
        b = (i * 2) % 11 + (i // 5)
        if a in ans:
            ans[a] = max(ans[a], b)
        else:
            ans[a] = b

    print(sum(ans.values()))


if __name__ == "__main__":
    main(10)