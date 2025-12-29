import math
import random


def main(n: int):
    # 根据规模 n 生成测试数据：
    # 生成两个不超过 2^n - 1 的非负整数 a, b（至少有一个非零）
    if n <= 0:
        a, b = 0, 0
    else:
        max_val = (1 << n) - 1
        a = random.randint(0, max_val)
        b = random.randint(0, max_val)
        if a == 0 and b == 0:
            # 保证不是全 0，避免一开始就退化为 0、0 的情况
            a = 1

    orig_a, orig_b = a, b  # 如果需要调试可用

    # 以下为原逻辑（去掉 input() 部分）
    while a != 0 and b != 0:
        x = int(math.log(a, 2))
        y = int(math.log(b, 2))
        if x != y:
            break
        a = a & (~(1 << x))
        b = b & (~(1 << y))

    if a == 0 and b == 0:
        print(0)
    else:
        if b > a:
            a, b = b, a
        x = int(math.log(a, 2)) + 1
        b = (1 << x) - 1
        a = a | b
        print(a)


# 示例调用（提交到评测系统时可删除或注释）
if __name__ == "__main__":
    main(10)