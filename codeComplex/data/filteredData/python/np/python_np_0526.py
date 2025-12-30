import random

def main(n):
    # 随机生成 k（1 到 min(7, n)）
    k = random.randint(1, min(7, n) if n > 0 else 1)
    # 随机生成长度为 n 的字符串，字符为前 k 个字母或 '?'
    chars = [chr(ord('a') + i) for i in range(k)]
    s_str = ''.join(random.choice(chars + ['?']) for _ in range(n))

    s = [-1 if c == "?" else ord(c) - 97 for c in s_str]

    def ok(m):
        nxt = [[n] * (n + 1) for _ in range(k)]
        for j in range(k):
            cnt = 0
            ni = n
            nxtj = nxt[j]
            for i in range(n - 1, -1, -1):
                if s[i] == -1 or s[i] == j:
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= m:
                    ni = i
                nxtj[i] = ni
        dp = [n + 1] * (1 << k)
        dp[0] = 0
        for bit in range(1 << k):
            l = dp[bit]
            if l + m > n:
                continue
            for j in range(k):
                if (bit >> j) & 1:
                    continue
                i = nxt[j][l]
                if i + m <= n:
                    nbit = bit | (1 << j)
                    if i + m < dp[nbit]:
                        dp[nbit] = i + m
        return dp[-1] <= n

    l, r = 0, n // k + 1
    while l + 1 < r:
        m = (l + r) // 2
        if ok(m):
            l = m
        else:
            r = m

    # 按需返回或打印结果，这里选择返回
    return l

if __name__ == "__main__":
    # 示例：调用 main(100)
    print(main(100))