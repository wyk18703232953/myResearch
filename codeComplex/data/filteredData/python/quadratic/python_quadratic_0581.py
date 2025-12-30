import random

def solve_one(n, k, s):
    p = (k + 2) // 2
    l = "RGB" * p
    res = n
    for i in range(n - k + 1):
        c = 0
        for j in range(0, k):
            c += (s[i + j] != l[j])
        res = min(res, c)

        c = 0
        for j in range(1, k + 1):
            c += (s[i + j - 1] != l[j])
        res = min(res, c)

        c = 0
        for j in range(2, k + 2):
            c += (s[i + j - 2] != l[j])
        res = min(res, c)
    return res


def main(n):
    # 根据规模 n 生成一组测试数据:
    # 随机选择 k（1 <= k <= n），并生成长度为 n 的字符串 s（字符集为 'R', 'G', 'B'）
    if n <= 0:
        return

    k = random.randint(1, n)
    s = ''.join(random.choice('RGB') for _ in range(n))

    ans = solve_one(n, k, s)
    print(ans)