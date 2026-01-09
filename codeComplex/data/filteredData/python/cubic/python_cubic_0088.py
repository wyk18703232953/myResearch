from collections import defaultdict

def main(n):
    # n controls the size of inputs:
    # k = min(10, max(1, n//3))
    # length of arrays c, f, h is n
    if n <= 0:
        return 0

    k = min(10, max(1, n // 3))

    # Deterministic generation of arrays:
    # Values in c and f are in [1, m], where m is also scaled with n
    m = max(1, n // 5)

    c = [(i % m) + 1 for i in range(n)]
    f = [((i * 2) % m) + 1 for i in range(n)]
    # h has length k+1, h[0] will be unused as in original code's h = [0] + ...
    h_list = [((i * 3) % (k + 5)) for i in range(k + 1)]
    h = h_list  # here h[0] is already defined and can be non-zero; logic uses h[j] for j<=k

    cnt1 = defaultdict(lambda: 0)
    for x in c:
        cnt1[x] += 1

    cnt2 = defaultdict(lambda: 0)
    for x in f:
        cnt2[x] += 1

    ans = 0
    for key in cnt2:
        c1, c2 = cnt1[key], cnt2[key]
        dp0 = [0]
        l = 1
        for _ in range(c2):
            dp = [0] * (l + k)
            for i in range(l):
                dp0i = dp0[i]
                for j in range(k + 1):
                    if i + j < len(dp):
                        candidate = dp0i + h[j]
                        if candidate > dp[i + j]:
                            dp[i + j] = candidate
            l += k
            dp0 = dp
        ans += dp[min(c1, k * c2)]

    return ans

if __name__ == "__main__":
    # Example deterministic call
    result = main(1000)
    # print(result)
    pass