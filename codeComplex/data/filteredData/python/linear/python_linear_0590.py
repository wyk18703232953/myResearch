import math
import random

def main(n):
    # 生成测试数据
    # 生成一个长度为 n 的 01 串 s
    s = [random.randint(0, 1) for _ in range(n)]
    # 随机生成查询个数 q（这里设为 n，必要时可调整策略）
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原始逻辑开始
    prefix = [0] * n
    prefix[0] = s[0]
    temp = [0] * (n + 1)
    temp[0] = 1
    mod = (pow(10, 9) // 1) + 7

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + s[i]
        temp[i] = (2 * (temp[i - 1] % mod)) % mod

    temp[n] = (2 * (temp[n - 1] % mod)) % mod

    ansarr = []
    for l, r in queries:
        l -= 1  # 转为 0-based
        r -= 1
        a = prefix[r] - prefix[l] + s[l]
        d = r - l + 1
        val1 = temp[d]
        val2 = temp[d - a]
        ansarr.append((val1 - val2) % mod)

    # 输出格式与原程序一致：每个答案一行
    print('\n'.join(map(str, ansarr)))


if __name__ == '__main__':
    # 可以在此处指定规模 n
    main(10)