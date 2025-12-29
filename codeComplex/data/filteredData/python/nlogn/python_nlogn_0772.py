import random

def main(n: int):
    # 生成测试数据：t 组测试，每组规模为 n
    t = 1  # 可根据需要调整测试组数
    results = []

    for _ in range(t):
        # 生成一组长度为 n 的随机整数数据
        # 数据范围可按需调整，这里假设为 [1, 10^9]
        li = [random.randint(1, 10**9) for _ in range(n)]

        li.sort()
        # 按原逻辑计算答案
        ans = min(li[n - 2] - 1, n - 2)
        results.append(ans)

    # 输出结果（与原代码行为一致：每组一行）
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)