import random

def main(n: int):
    """
    n 用来控制测试数据规模（这里理解为 a,b 的上界规模 ~ 2^n）。
    逻辑：原程序通过交互 qu(a,b) 来比较隐藏的 A,B。
    这里我们根据 n 生成随机的 A,B，直接在 qu 中模拟比较。
    """

    # 随机生成隐藏的 A,B，范围 [0, 2^n - 1]
    limit = 1 << n
    A = random.randrange(limit)
    B = random.randrange(limit)

    # 用于调试/验证：可打印出来查看
    # print("Hidden A,B =", A, B)

    def qu(a: int, b: int) -> int:
        """
        模拟原来的交互比较函数：
        返回 sign((A - a) - (B - b))，即：
        (A - a) > (B - b) ->  1
        (A - a) == (B - b) -> 0
        (A - a) < (B - b) -> -1
        """
        va = A - a
        vb = B - b
        if va > vb:
            return 1
        elif va < vb:
            return -1
        else:
            return 0

    a = 0
    b = 0
    big = qu(a, b)

    # 按原逻辑从最高位到最低位依次尝试设置比特
    for i in range(29, -1, -1):
        x = 1 << i
        f = qu(a + x, b)
        l = qu(a, b + x)
        if l == f:
            if big == 1:
                a += x
            else:
                b += x
            big = f
        elif f == -1:
            a += x
            b += x

    # 输出推断出的 a, b 及真实的 A, B 以便验证
    print("Guessed a,b:", a, b)
    print("Real    A,B:", A, B)


if __name__ == "__main__":
    # 示例：用 n=30 作为规模（与原程序 0..29 位一致）
    main(30)