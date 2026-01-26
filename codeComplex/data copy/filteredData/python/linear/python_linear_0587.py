def main(n):
    mod = 10**9 + 7

    # scale n to avoid over-allocating pow2; ensure at least 1
    n = max(1, int(n))

    # define problem size in terms of original variables
    # we choose:
    #   seq length = n
    #   number of queries q = n
    seq_len = n
    q = n

    # deterministically generate the bit string l of length seq_len
    # simple pattern based on index: 1 if i is even, 0 otherwise
    l = ''.join('1' if i % 2 == 0 else '0' for i in range(seq_len))

    cnt1, cnt0 = [0] * (seq_len + 1), [0] * (seq_len + 1)

    for i in range(len(l)):
        if l[i] == '1':
            cnt1[i + 1] = cnt1[i] + 1
            cnt0[i + 1] = cnt0[i]

        else:
            cnt0[i + 1] = cnt0[i] + 1
            cnt1[i + 1] = cnt1[i]

    # precompute powers of 2 up to maximum possible ones or zeroes
    max_len = seq_len
    pow2 = [1] * (max_len + 1)
    for i in range(1, max_len + 1):
        pow2[i] = (2 * pow2[i - 1]) % mod

    results = []

    # deterministically generate q queries (l, r), 1-based inclusive
    # choose segments that cover varying ranges but always valid
    for i in range(q):
        # map i to a segment [L, R]
        L = (i % seq_len) + 1
        length = (i // 2) % seq_len + 1
        R = L + length - 1
        if R > seq_len:
            R = seq_len
        if L > R:
            L, R = R, L

        ones = cnt1[R] - cnt1[L - 1]
        zeroes = cnt0[R] - cnt0[L - 1]
        t1 = (pow2[ones] - 1) % mod
        t2 = (t1 * (pow2[zeroes] - 1)) % mod
        results.append((t1 + t2) % mod)

    # to keep behavior similar to original script, print all answers
    for ans in results:
        # print(ans)
        pass

    return results


if __name__ == "__main__":
    # example deterministic call; adjust n as needed for experiments
    main(10)