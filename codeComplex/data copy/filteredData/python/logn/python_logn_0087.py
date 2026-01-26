import math


def main(n):
    # 生成确定性的输入 a, b，随 n 变化规模增大
    # 这里令 a, b 都在 [1, 2^n - 1] 范围内，且构造方式确定
    if n <= 1:
        # 保证非零，避免立即退出循环
        a = 1
        b = 1

    else:
        a = (1 << n) - 1          # 全 1 的 n 位数
        b = (1 << (n - 1)) + 1    # 最高位和最低位为 1 的 n 位数

    a_orig, b_orig = a, b

    # 原核心逻辑
    while a != 0 and b != 0:
        x = int(math.log(a, 2))
        y = int(math.log(b, 2))
        if x != y:
            break
        a = a & (~(1 << x))
        b = b & (~(1 << y))

    if a == 0 and b == 0:
        result = 0

    else:
        if b > a:
            a, b = b, a
        x = int(math.log(a, 2)) + 1
        b = (1 << x) - 1
        a = a | b
        result = a

    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例：用不同规模调用 main
    for n in range(1, 6):
        main(n)