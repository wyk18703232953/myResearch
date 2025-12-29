def main(n):
    # 原逻辑封装为函数
    def calc(val):
        if val == 1 or val == 2:
            return val
        elif val & 1:  # 奇数
            return val * (val - 1) * (val - 2)
        else:  # 偶数
            if val % 3 == 0:
                return (val - 2) * (val - 1) * (val - 3)
            else:
                return max(
                    val * (val - 1) * (val - 3),
                    (val - 1) * (val - 2) * (val - 3),
                    (val * (val - 1) * (val - 2)) / 2,
                )

    # 根据规模 n 生成测试数据，这里简单设为测试 val 从 1 到 n
    results = []
    for val in range(1, n + 1):
        results.append((val, calc(val)))

    # 输出测试结果
    for val, ans in results:
        print(f"n={val}, result={ans}")


if __name__ == "__main__":
    # 示例：可调整这里的 n 以改变测试规模
    main(10)