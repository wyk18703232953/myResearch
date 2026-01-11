def main(n):
    # Interpret n as the size parameter:
    # - number of elements in s is n
    # - number of elements in s1 is m = n (same scale for simplicity)
    # Generate deterministic data for s and s1
    # s: increasing sequence with small values
    # s1: larger values to often satisfy min(s1) >= max(s)
    m = n if n > 0 else 1

    # Generate s as [1, 2, ..., n]
    s = [i + 1 for i in range(n)]

    # Generate s1 deterministically based on n and index
    # Ensure values are generally larger than s to avoid trivial -1 outputs
    # For example: s1[i] = (i + 1) * 2
    s1 = [(i + 1) * 2 for i in range(m)]

    if not s or not s1:
        # print(0)
        pass
        return

    if min(s1) < max(s):
        # print(-1)
        pass
        return

    s.sort()
    s1.sort()

    ans = 0
    if s1[0] != s[-1]:
        ans += s1[0]
        ans += s[-2] * (m - 1)
        ans += sum(s1[1::])
        ans += s[-1]
        for i in range(n - 2):
            ans += s[i] * m

    else:
        ans += sum(s1)
        for i in range(n - 1):
            ans += s[i] * m

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)