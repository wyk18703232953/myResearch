import random


def bit_count(x):
    ans = 0
    while x:
        x &= x - 1
        ans += 1
    return ans


def solve(n_str, k):
    n = n_str
    x = len(n)
    if n == '1':
        return int(k == 0)
    if not k:
        return 1
    mod = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[1] = 1
    for i in range(2, x + 1):
        dp[i] = dp[bit_count(i)] + 1
    dp1 = [[0] * (x + 1) for _ in range(x + 1)]
    # length ; set bits
    for i in range(x + 1):
        dp1[i][0] = 1
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            dp1[i][j] = (dp1[i - 1][j - 1] + dp1[i - 1][j]) % mod
    ans = 0
    cou = n.count('1')
    for i in range(1, x + 1):
        if dp[i] != k:
            continue
        se = i
        for j in range(x):
            if n[j] == '0':
                continue
            ans = (ans + dp1[x - 1 - j][se] - (se == 1 and k == 1)) % mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans + 1) % mod
    return ans


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       我们生成一个长度为 n 的随机二进制串 n_str 和一个随机 k。
    返回：根据原逻辑计算出的答案。
    """
    if n <= 0:
        n = 1

    # 生成长度为 n 的随机二进制串，避免全为 0，至少有一位是 1
    bits = [random.choice('01') for _ in range(n)]
    if all(b == '0' for b in bits):
        bits[random.randrange(n)] = '1'
    n_str = ''.join(bits)

    # k 的取值不需要特别大，这里设为 [0, n] 范围内的随机整数
    k = random.randint(0, n)

    return solve(n_str, k)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行一次测试
    ans = main(10)
    print(ans)