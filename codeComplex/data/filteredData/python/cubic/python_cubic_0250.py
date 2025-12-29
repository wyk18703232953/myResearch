import random

def main(n):
    # 1. 根据规模 n 生成 ri, gi, bi（这里简单设为都等于 n）
    ri = gi = bi = n

    # 2. 生成测试数据：ri, gi, bi 个正整数
    #   为了便于测试，使用 1~100 的随机整数
    rr = sorted(random.randint(1, 100) for _ in range(ri))
    gr = sorted(random.randint(1, 100) for _ in range(gi))
    br = sorted(random.randint(1, 100) for _ in range(bi))

    # 3. 初始化 DP 数组
    dp = [[[-1] * (bi + 1) for _ in range(gi + 1)] for _ in range(ri + 1)]

    # 4. 原逻辑封装为内部函数
    def area(r, g, b):
        # 使用偏移量 +1 防止索引为 -1
        if dp[r + 1][g + 1][b + 1] != -1:
            return dp[r + 1][g + 1][b + 1]
        ans = 0
        if r >= 0 and g >= 0:
            ans = max(ans, rr[r] * gr[g] + area(r - 1, g - 1, b))
        if r >= 0 and b >= 0:
            ans = max(ans, rr[r] * br[b] + area(r - 1, g, b - 1))
        if b >= 0 and g >= 0:
            ans = max(ans, br[b] * gr[g] + area(r, g - 1, b - 1))
        dp[r + 1][g + 1][b + 1] = ans
        return ans

    # 5. 返回结果（也可以选择 print）
    result = area(ri - 1, gi - 1, bi - 1)
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)