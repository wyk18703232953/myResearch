def main(n):
    # n: input size, interpreted as length of arrays s and c
    if n < 3:
        print(-1)
        return

    # Deterministically generate s and c of length n
    # s is a simple increasing sequence with some pattern
    # c is a cost pattern derived from s and indices
    s = [i * 2 + (i % 3) for i in range(n)]
    c = [(i * i + 3 * i + 7) % 1000 + 1 for i in range(n)]

    maxx = float('inf')
    ans = maxx

    for mid in range(1, n - 1):
        l = [maxx] + [c[i] for i in range(mid) if s[i] < s[mid]]
        r = [maxx] + [c[i] for i in range(mid + 1, n) if s[i] > s[mid]]
        left_min = min(l)
        right_min = min(r)
        candidate = left_min + c[mid] + right_min
        if candidate < ans:
            ans = candidate

    print(ans if ans != float('inf') else -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n here for experiments
    main(10)