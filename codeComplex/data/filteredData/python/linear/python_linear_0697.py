def main(n: int):
    # 生成测试数据：v 范围设为 [1, n]，这里简单设为 v = n // 2 或至少为 1
    v = max(1, n // 2)

    remaining_dist = n - 1
    adding = min(remaining_dist, v)
    cost = adding

    remaining_dist -= adding

    i = 2
    while remaining_dist > 0:
        cost += i
        i += 1
        remaining_dist -= 1

    # print(cost)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)