MOD = 1000000007


def find(c: str) -> int:
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 26

    else:
        return ord(c) - ord('a')


def add(a: int, b: int) -> int:
    a += b
    if a >= MOD:
        a -= MOD
    return a


def sub(a: int, b: int) -> int:
    a -= b
    if a < 0:
        a += MOD
    return a


def main(n: int):
    """
    生成长度为 n 的测试串 s，随机逻辑可按需替换。
    这里给出一个确定性构造：循环使用 'a'-'z','A'-'Z'。
    同时生成若干查询 (x, y)。
    返回：(s, queries, answers)
    """

    # 1. 生成测试数据：字符串 s
    # 字母表：26 小写 + 26 大写，共 52 种
    letters = [chr(ord('a') + i) for i in range(26)] + \
              [chr(ord('A') + i) for i in range(26)]
    if n <= 0:
        return "", [], []

    s_chars = [letters[i % 52] for i in range(n)]
    s = "".join(s_chars)

    # 2. 预处理与原程序一致
    length = len(s)
    buc = [0] * 101
    fac = [0] * (length + 1)
    inv = [0] * (length + 1)
    dp = [0] * (length + 1)
    ans = [[0] * 55 for _ in range(55)]

    # 计数
    for ch in s:
        buc[find(ch)] += 1

    # 阶乘和逆元
    fac[0] = 1
    for i in range(1, length + 1):
        fac[i] = (fac[i - 1] * i) % MOD
    inv[length] = pow(fac[length], MOD - 2, MOD)
    for i in range(length - 1, -1, -1):
        inv[i] = (inv[i + 1] * (i + 1)) % MOD

    num = pow(fac[length // 2], 2, MOD)
    for i in range(52):
        num = (num * inv[buc[i]]) % MOD

    dp[0] = 1
    for i in range(52):
        if not buc[i]:
            continue
        for j in range(length, buc[i] - 1, -1):
            dp[j] = add(dp[j], dp[j - buc[i]])

    for i in range(52):
        ans[i][i] = dp[length // 2]

    for i in range(52):
        if not buc[i]:
            continue
        temp_dp = dp.copy()
        for k in range(buc[i], length + 1):
            temp_dp[k] = sub(temp_dp[k], temp_dp[k - buc[i]])

        for j in range(i + 1, 52):
            if not buc[j]:
                continue
            for k in range(buc[j], length + 1):
                temp_dp[k] = sub(temp_dp[k], temp_dp[k - buc[j]])

            ans[i][j] = (2 * temp_dp[length // 2]) % MOD

            for k in range(length, buc[j] - 1, -1):
                temp_dp[k] = add(temp_dp[k], temp_dp[k - buc[j]])

    # 3. 构造查询：这里构造 n 个简单查询 (i, n-i+1)
    q = n
    queries = []
    for i in range(1, n + 1):
        x, y = i, n - i + 1
        queries.append((x, y))

    # 4. 计算每个查询的答案（不打印，返回）
    answers = []
    for x, y in queries:
        l = find(s[x - 1])
        r = find(s[y - 1])
        if l > r:
            l, r = r, l
        answers.append(num * ans[l][r] % MOD)

    return s, queries, answers


# 示例调用（评测时可以移除或忽略）
if __name__ == "__main__":
    s, queries, answers = main(10)
    # print("s =", s)
    pass
    # print("queries =", queries)
    pass
    # print("answers =", answers)
    pass