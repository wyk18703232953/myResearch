import random

# 常量与工具函数（保留以便可能扩展）
ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 10**9 + 7
EPS = 1e-6


def main(n: int):
    """
    n 为生成测试数据规模参数，这里用于控制随机数范围。
    逻辑：给定 l, r，找到满足 l <= x <= r 的所有 x 中，
    其最大可能值与 l 的按位异或范围（原题实质为：若 l 与 r 在第 i 位上不同，
    则答案为 2^(i+1)-1 中最大那个）。
    """

    # 1. 根据 n 生成测试数据
    # 这里设定：r 在 [0, 2^n - 1] 范围内，l 在 [0, r] 范围内
    if n <= 0:
        n = 1
    max_val = (1 << min(n, 60)) - 1  # 防止位数过大，这里限制为最多 60 位
    r = random.randint(0, max_val)
    l = random.randint(0, r)

    # 2. 原始逻辑
    ans = 0
    # 原代码冗余变量 R = len(bin(r)) - 2 未使用，这里删除
    for i in range(61):
        if (l & (1 << i)) ^ (r & (1 << i)):
            ans = (1 << (i + 1)) - 1

    # 3. 输出结果
    # 如果希望看到测试数据本身，可打印 l, r
    print(f"l = {l}, r = {r}, ans = {ans}")


if __name__ == "__main__":
    # 示例：调用 main，n 控制数据规模
    main(10)