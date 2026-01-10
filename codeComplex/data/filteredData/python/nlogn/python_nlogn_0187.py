def main(n):
    N = n
    if N <= 0:
        print(0)
        return

    # Deterministic data generation: A is a list of length N
    # Example pattern: A[i] = (i % 5) - 2, producing values in {-2, -1, 0, 1, 2}
    A = [(i % 5) - 2 for i in range(N)]

    from collections import defaultdict

    sum_A = sum(A)
    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1

    ans = 0
    for i in range(N):
        a = A[i]
        cnt[a] -= 1
        sum_A -= a

        tmp = sum_A
        n_local = 0
        for b in (a - 1, a, a + 1):
            n_local += cnt[b]
            tmp -= b * cnt[b]
        ans += tmp - a * (N - 1 - i - n_local)
    print(ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10)