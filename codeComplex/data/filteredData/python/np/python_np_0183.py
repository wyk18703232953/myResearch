def main(n):
    # 1. 生成测试数据
    # 为了构造一个合理的测试环境，这里:
    # - arr 为 1 到 n 的递增数组
    # - 区间 [l, r] 设为所有元素和的一部分区间
    # - x 设为一个与 n 相关的差值阈值
    arr = list(range(1, n + 1))

    total_sum = sum(arr)
    # 设一个中等宽度的区间 [l, r]
    l = total_sum // 4
    r = total_sum * 3 // 4
    # 要求最大值与最小值至少相差 x
    x = max(1, n // 3)

    res = 0
    # 2^n 种非空子集的枚举
    for mask in range(1, 1 << n):
        subset = [arr[i] for i in range(n) if (mask >> i) & 1]
        s = sum(subset)
        if l <= s <= r and max(subset) - min(subset) >= x:
            res += 1

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)