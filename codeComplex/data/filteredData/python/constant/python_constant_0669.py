import random

def main(n):
    """
    将交互式程序改为本地模拟：
    - n 为比特位数规模（原程序固定为 30，可改为任意正整数）
    - 随机生成两个整数 x, y（0 <= x, y < 2^n）
    - 通过模拟交互（? a b -> sign((x^a) - (y^b))）来恢复 x, y
    - 最终输出推断得到的 a, b（应等于 x, y）
    """
    # 随机生成隐藏的 x, y
    max_val = 1 << n
    x = random.randrange(max_val)
    y = random.randrange(max_val)

    # 模拟交互：给定 a, b，返回 sign( (x ^ a) - (y ^ b) )
    def query(a, b):
        val = (x ^ a) - (y ^ b)
        if val > 0:
            return 1
        elif val < 0:
            return -1
        else:
            return 0

    # 初始查询，对应原代码中的：
    # print("? 0 0"); t = int(input())
    t = query(0, 0)

    A = [-1] * n
    B = [-1] * n
    a = 0
    b = 0

    # 第一阶段：从最高位到最低位处理
    i = n - 1
    d = 1 << i
    while i >= 0:
        a += d
        b += d
        s = query(a, b)

        # 原代码条件：if s == -t:
        if s == -t:
            # 下面两种分支实质上用第二次查询来更新 t 并确定该位
            if s == 1:
                A[i] = 0
                B[i] = 1
                b -= d
                t = query(a, b)
            elif s == -1:
                A[i] = 1
                a -= d
                B[i] = 0
                t = query(a, b)

        i -= 1
        d //= 2

    # 第二阶段：处理仍为 -1 的位（那些两数在该位相同的情况）
    d = 1
    for j in range(n):
        if A[j] == -1:
            a ^= d
            s = query(a, b)
            if s == 1:
                A[j] = 1
                B[j] = 1
            else:
                A[j] = 0
                B[j] = 0
            a ^= d
        d <<= 1

    # 根据位数组 A, B 还原整数 a, b
    d = 1
    a = 0
    b = 0
    for i in range(n):
        a += d * A[i]
        b += d * B[i]
        d <<= 1

    # 输出推断结果 a, b，以及真实的 x, y 便于验证
    print("inferred:", a, b)
    print("actual:  ", x, y)


if __name__ == "__main__":
    # 示例：使用原题规模 n = 30
    main(30)