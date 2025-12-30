import random
from typing import List, Tuple


def main(n: int):
    """
    规模说明：
    - n 为数组长度
    - 自动生成：
      * arr: 长度为 n 的随机整数数组
      * ops: 长度为 2n 的操作序列，由 n 个 '0' 和 n 个 '1' 构成，
             且保证栈操作合法：任意前缀中 '1' 的数量不超过 '0'
    """
    # 1. 生成测试数据：数组 arr
    # 这里生成 1..10^9 范围的随机整数，也可以按需要调整
    arr = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 生成合法操作序列 ops（模拟原代码中对 input() 的那一行）
    #    使用一个简单的随机游走：在保证不违规的前提下随机选择 '0' 或 '1'
    zeros_used = 0
    ones_used = 0
    ops: List[str] = []
    total = 2 * n
    for _ in range(total):
        # 还可以放入 '0' 的条件：zeros_used < n
        # 可以放入 '1' 的条件：ones_used < zeros_used
        can_zero = zeros_used < n
        can_one = ones_used < zeros_used
        if can_zero and can_one:
            if random.randint(0, 1) == 0:
                ops.append('0')
                zeros_used += 1
            else:
                ops.append('1')
                ones_used += 1
        elif can_zero:
            ops.append('0')
            zeros_used += 1
        else:
            # 只能放 '1'
            ops.append('1')
            ones_used += 1

    # 3. 以下为对原逻辑的等价实现

    # arr 带上原来的索引
    arr_enum: List[Tuple[int, int]] = list(enumerate(arr))
    # 按值排序
    arr_enum.sort(key=lambda x: x[1])

    i = 0
    stack: List[Tuple[int, int]] = []
    output_indices: List[int] = []

    for ch in ops:
        if ch == '0':
            stack.append(arr_enum[i])
            output_indices.append(arr_enum[i][0] + 1)
            i += 1
        else:
            x = stack.pop()
            output_indices.append(x[0] + 1)

    # 按原程序格式打印结果：同一行用空格分隔
    print(" ".join(map(str, output_indices)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)