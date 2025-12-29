import random

def main(n: int):
    # 生成测试轮数 t
    t = max(1, n)

    # 生成 t 组测试数据，并输出对应结果
    for _ in range(t):
        # 为每组测试生成长度为 n 的数组
        # 数值范围可根据需要调整，这里设为 1 ~ 10^9
        a = [random.randint(1, 10**9) for _ in range(n)]

        # 保持与原逻辑一致：对 a 排序并计算答案
        a_sorted = sorted(a, reverse=True)
        # 确保 n >= 2 时 a_sorted[1] 有意义；若 n < 2，则结果定义为 0
        if n >= 2:
            ans = min(n - 2, a_sorted[1] - 1)
        else:
            ans = 0
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)