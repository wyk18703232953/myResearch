memo = {}

def max_splits(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    result = 4 * max_splits(n - 1) + 1
    memo[n] = result
    return result


def main(n):
    """
    n 为测试规模，这里将其作为测试用例数量 t，
    并为每个用例生成 (n_i, k_i) 测试数据。
    生成规则可以按需调整。
    """

    t = n  # 测试用例数量
    cases = []

    # 生成测试数据：第 i 个用例使用 n_i = i+1, k_i = (i+1)^2 之类的简单构造
    for i in range(t):
        ni = i + 1
        # 让 k 在一个比较合理的范围内变化
        # 可覆盖小值和较大值
        if ni <= 5:
            ki = ni  # 小规模时让 k 较小
        else:
            ki = ni * ni // 2  # 稍大一些
        cases.append((ni, ki))

    outputs = []
    for (n_val, k) in cases:
        global memo
        memo = {}  # 每个用例清空 memo，保持与原逻辑一致

        min_splits = 1
        path_count = 3

        if n_val > 75:
            outputs.append(f"YES {n_val - 1}")
            continue

        square_size = n_val - 1
        max_buffer = max_splits(square_size)

        while min_splits + path_count <= k and square_size > 0:
            min_splits += path_count
            max_buffer += (4 * path_count - (2 * path_count + 1)) * max_splits(square_size - 1)
            path_count = 2 * path_count + 1
            square_size -= 1

        if min_splits <= k <= min_splits + max_buffer:
            outputs.append(f"YES {square_size}")
        else:
            outputs.append("NO")

    # 输出所有结果
    for line in outputs:
        print(line)


# 示例: 直接运行 main(5) 做简单自测
if __name__ == "__main__":
    main(5)