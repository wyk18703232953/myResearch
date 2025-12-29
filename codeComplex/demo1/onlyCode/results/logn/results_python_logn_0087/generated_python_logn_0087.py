import math
import random


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 生成两个在 [1, 2^n - 1] 范围内的正整数 a, b
    if n <= 0:
        return

    max_val = (1 << n) - 1
    a = random.randint(1, max_val)
    b = random.randint(1, max_val)

    # 原始逻辑开始
    aa, bb = a, b  # 如需调试可保留原始值

    while aa != 0 and bb != 0:
        x = int(math.log(aa, 2))
        y = int(math.log(bb, 2))
        if x != y:
            break
        aa = aa & (~(1 << x))
        bb = bb & (~(1 << y))

    if aa == 0 and bb == 0:
        print(0)
    else:
        if bb > aa:
            aa, bb = bb, aa
        x = int(math.log(aa, 2)) + 1
        bb = (1 << x) - 1
        aa = aa | bb
        print(aa)


if __name__ == "__main__":
    # 示例调用：n 可以根据需要调整
    main(10)