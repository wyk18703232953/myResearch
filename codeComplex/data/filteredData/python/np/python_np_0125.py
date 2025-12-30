import math
import random

def main(n):
    # 生成测试数据：
    # b 和 c 都为长度为 n 的正整数数组
    # 这里给出一种简单生成方式，可根据需要修改
    random.seed(0)
    b = [random.randint(1, 10 * n) for _ in range(n)]
    c = [random.randint(1, 10 * n) for _ in range(n)]

    dp = {0: 0}
    s = {0}

    for i in range(n):
        # 为避免在遍历时修改原 dp，使用临时字典保存更新
        new_dp = dict(dp)
        for j in s:
            g = math.gcd(j, b[i])
            cost = dp[j] + c[i]
            if g in new_dp:
                if cost < new_dp[g]:
                    new_dp[g] = cost
            else:
                new_dp[g] = cost
        dp = new_dp
        s = set(dp.keys())

    if 1 in dp:
        print(dp[1])
    else:
        print(-1)


if __name__ == "__main__":
    # 这里给一个默认规模，可按需要修改或在外部调用 main(n)
    main(5)