from collections import defaultdict as dd
import math

def main(n):
    # 根据 n 构造确定性输入规模
    # 映射为原程序中的 n, v
    # 使得两种分支（v >= n-1 和 v < n-1）都可被覆盖随 n 变化时
    N = n + 2  # 保证 N >= 2
    # v 在 [0, 2N) 内循环变化，保证有时大于等于 N-1，有时小于
    v = (3 * n) % (2 * N)

    # 原始核心逻辑
    dist = N - 1
    if v >= dist:
        result = dist

    else:
        off = dist - v
        prices = [i + 2 for i in range(off)]
        result = v + sum(prices)

    # 为了完整性，返回结果
    return result

if __name__ == "__main__":
    # 示例调用，可按需修改 n 用于时间复杂度实验
    for n in range(1, 10):
        # print(n, main(n))
        pass