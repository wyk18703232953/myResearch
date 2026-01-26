def main(n):
    MOD = 1000000007

    # 根据规模 n 生成测试数据：
    # 这里假设：x = n，k = n（可按需要自行调整生成规则）
    x = n
    k = n

    twoPow = pow(2, k, MOD)

    minQ = max(0, (x * twoPow - twoPow + 1))
    minQ *= 2

    maxQ = x * twoPow * 2

    ans = ((maxQ * (maxQ + 1) // 2 - minQ * (minQ + 1) // 2 + minQ) //
           (maxQ - minQ + 1)) % MOD

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改
    main(10)