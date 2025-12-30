from math import gcd
import random

mod = 998244353
INF = float('inf')


def main(n):
    # 1. 生成测试数据
    # 这里根据规模 n 构造 larr, carr
    # 可按需要修改生成策略
    random.seed(0)
    # larr 用 1~100 的正整数，carr 用 1~100 的正整数
    larr = [random.randint(1, 100) for _ in range(n)]
    carr = [random.randint(1, 100) for _ in range(n)]

    # 2. 原逻辑
    dic = {0: 0}

    for i in range(n):
        l, c = larr[i], carr[i]
        ndic = dic.copy()
        for j in dic:
            now = gcd(j, l)
            if now not in ndic:
                ndic[now] = c + dic[j]
            else:
                ndic[now] = min(ndic[now], dic[j] + c)
        dic = ndic

    ans = dic.get(1, -1)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)