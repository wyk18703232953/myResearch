def solve(d, n, k):
    mv = sum(d[0:k])
    v = mv
    for i in range(1, n - k + 1):
        mv = mv + d[i + k - 1] - d[i - 1]
        v = min(v, mv)
    return v

def run_single_case(n, k, s):
    st = 'RGB' * (n // 3 + 3)
    diff1 = [0 for _ in range(n)]
    diff2 = [0 for _ in range(n)]
    diff3 = [0 for _ in range(n)]

    for i in range(n):
        if s[i] != st[i]:
            diff1[i] = 1
        if s[i] != st[i + 1]:
            diff2[i] = 1
        if s[i] != st[i + 2]:
            diff3[i] = 1

    return min(solve(diff1, n, k), solve(diff2, n, k), solve(diff3, n, k))

def main(n):
    # n: total "input size" controlling number of test cases and length of each string
    # Deterministically map n -> T, each (n_i, k_i, s_i)
    if n <= 0:
        return

    T = max(1, n // 10)
    base_len = max(1, n // T)
    results = []

    for t in range(T):
        cur_n = base_len + (t % 5)
        k = 1 + (t % cur_n)

        s_chars = []
        for i in range(cur_n):
            s_chars.append("RGB"[(i + t) % 3])
        s = "".join(s_chars)

        res = run_single_case(cur_n, k, s)
        results.append(res)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(30)