from collections import Counter
import random

def main(n):
    # 1. 生成测试数据
    # 生成 n 个正整数，长度不超过 10 位
    # 同时生成一个 k（1 <= k <= 10^9，避免为 0）
    k = random.randint(1, 10**9)
    a1 = [random.randint(1, 10**10 - 1) for _ in range(n)]
    a = [str(x) for x in a1]

    # 2. 原始逻辑（去掉 input，使用生成的数据）
    dct = [Counter() for _ in range(11)]
    for i in range(n):
        dct[len(a[i])][a1[i] % k] += 1

    ans = 0
    for i in range(n):
        x = a1[i]
        for j in range(1, 11):
            x = (x * 10) % k
            if x:
                ans += dct[j][k - x]
            else:
                ans += dct[j][0]
        if not (a1[i] * (pow(10, len(a[i]), k) + 1)) % k:
            ans -= 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)