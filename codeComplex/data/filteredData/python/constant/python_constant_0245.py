import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里令 n 即为原程序中的 n（幂的次数），
    # m 取一个与 2^n 同数量级的随机整数，保证有一定覆盖度。
    if n <= 0:
        # 原程序对 n<=0 情况未定义，这里简单处理为不输出或默认值
        return

    # 生成 m：在 [1, 2^(n+1)) 范围内随机取值，以涵盖多种情况
    max_m = 2 ** (n + 1)
    m = random.randint(1, max_m)

    r = 1
    for power in range(n):
        r *= 2
        if r > m:
            print(m)
            break
    else:
        if r == m:
            print(0)
        else:
            print(m % r)


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可在其他地方调用 main(n)
    main(5)