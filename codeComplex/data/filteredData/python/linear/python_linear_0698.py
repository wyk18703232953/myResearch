def main(n):
    # 生成测试数据：给定规模 n，构造一个合理的 v
    # v 的上限不能超过 n-1（否则 v-fuel 很快用不完，直接取 n-1 比较合理）
    if n <= 1:
        # 对于 n<=1，原算法循环不会执行，这里直接输出 0
        print(0)
        return

    v = n - 1  # 可以根据需要调整生成策略

    res = 0
    fuel = 0
    for i in range(1, n):
        miss = min(v - fuel, n - i - fuel)
        # 如果 miss <= 0，后续 fuel 只会越来越大，n-i-fuel 越来越小，不会再有贡献
        if miss <= 0:
            break
        res += i * miss
        fuel += miss - 1
        if v - fuel == 0:
            print(res)
            return
    print(res)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)