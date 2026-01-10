def main(n):
    # Interpret n as N (input size)
    N = n
    if N <= 0:
        print(0)
        return

    # Deterministic generation of A: simple increasing sequence with some variation
    # Example: A[i] = (i * 2 + (i // 3)) % (2 * N + 5)
    A = [(i * 2 + (i // 3)) % (2 * N + 5) for i in range(N)]

    bit = []
    nax = 200010
    for _ in range(nax * 4 + 1):
        bit.append([0, 0])

    def up(k, val):
        while k < (nax * 4):
            bit[k][0] += val
            bit[k][1] += 1
            k += (k & -k)

    def go(k):
        ans = 0
        r = 0
        while k > 0:
            ans += bit[k][0]
            r += bit[k][1]
            k -= (k & -k)
        return ans, r

    index = {}
    B = [x for x in A]
    B.sort()
    idx = 1
    index[B[0]] = idx
    for i in range(1, N):
        if B[i] != B[i - 1]:
            if B[i] == (B[i - 1] + 1):
                idx += 1
                index[B[i]] = idx
            else:
                idx += 2
                index[B[i]] = idx

    have = 0
    for i in range(0, N):
        a1, a2 = go(index[A[i]] - 2)
        a3, a4 = go(3 * N)
        a5, a6 = go(index[A[i]] + 1)
        s1 = (a2 * A[i]) - (a1)
        s2 = ((a4 - a6) * A[i]) - (a3 - a5)
        have += s1
        have += s2
        up(index[A[i]], A[i])

    print(have)


if __name__ == "__main__":
    # Example deterministic call for testing / benchmarking
    main(1000)