import random

def main(n):
    # 生成测试数据：
    # t 为测试组数，这里让 t = n
    # 每组长度也设为 n，并生成升序数组
    t = n
    test_cases = []
    for _ in range(t):
        # 生成 n 个随机正整数
        arr = [random.randint(1, 10**9) for _ in range(n)]
        arr.sort()
        test_cases.append((n, arr))

    # 逻辑与原始程序保持一致
    for n_val, d in test_cases:
        # 原代码: d = sorted(li())，已经在生成时排序
        # print(min(d[-2] - 1, n - 2))
        if n_val < 2:
            # 原代码在 n<2 时行为未定义，这里简单保护
            print(0)
        else:
            print(min(d[-2] - 1, n_val - 2))


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)