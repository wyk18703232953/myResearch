def main(n):
    # Deterministic generation of N, K, S from n
    # Ensure N >= K >= 1
    if n < 1:
        n = 1
    K = max(1, n % 5 + 1)  # K in [1,5]
    N = max(K, n * 3)      # N scales linearly with n, and N >= K

    # Generate a deterministic pattern string of length N over 'a'..(a+K-1) and '?'
    # Use simple arithmetic, no randomness
    chars = []
    for i in range(N):
        v = (i * 7 + 3) % (K + 1)  # value in [0, K]
        if v == K:
            chars.append('?')
        else:
            chars.append(chr(ord('a') + v))
    S = ''.join(chars)

    # Convert S as in the original code
    S_list = [-1 if _ == '?' else ord(_) - ord('a') for _ in S]

    def check(x):
        p = [[N for _ in range(N + 1)] for _ in range(K)]

        for k in range(K):
            keep = 0
            for i in range(N - 1, -1, -1):
                keep += 1
                if S_list[i] != -1 and S_list[i] != k:
                    keep = 0
                p[k][i] = p[k][i + 1]
                if keep >= x:
                    p[k][i] = i + x - 1

        d = [N for _ in range(1 << K)]
        d[0] = -1
        for s in range(1, 1 << K):
            for k in range(K):
                if (s & (1 << k)) and (d[s ^ (1 << k)] < N):
                    d[s] = min(d[s], p[k][d[s ^ (1 << k)] + 1])
        return d[(1 << K) - 1] < N

    l, r = 0, N // K
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1

    print(l)


if __name__ == "__main__":
    main(10)