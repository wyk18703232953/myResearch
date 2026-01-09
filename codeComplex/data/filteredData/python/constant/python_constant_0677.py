def main(n):
    """
    将交互式程序改为可本地测试的版本。
    n 作为规模，表示要猜测的整数的比特长度（原代码中固定为 30）。

    我们在本地生成一个隐藏的 (A, B)，然后用原逻辑通过“询问”来恢复 (a, b)，
    最终返回推测结果和真实值，便于验证正确性。
    """

    # 生成测试数据：隐藏的真实 A, B（0 <= A, B < 2^n）
    # 你可以根据需求修改生成规则（例如随机、固定等）
    A = (1 << (n - 1)) - 1  # 示例：全 1（二进制）但不超过 2^n-1
    B = (1 << (n - 2))      # 示例：只有第 n-1 位为 1

    # 定义“交互”函数：模拟判题机返回 -1 / 0 / 1
    # 原题是比较 A^2 与 B^2 的大小，但此处原代码含义未知。
    # 假设比较 (A XOR x)^2 与 (B XOR y)^2 的大小，只作示例。
    # 如果你有真实题意，可根据实际比较逻辑修改此函数。
    def judge(x, y):
        # 示例逻辑：比较 (A - x)^2 与 (B - y)^2
        left = (A - x) ** 2
        right = (B - y) ** 2
        if left < right:
            return -1
        elif left > right:
            return 1

        else:
            return 0

    m = n
    a, b = 0, 0
    fle = 1

    # 为了观察行为，记录所有“询问与回答”，最终可打印或返回
    queries = []

    for i in range(m):
        if fle:
            # 对应原来的：print('? a b'); resp1 = int(raw_input())
            resp1 = judge(a, b)
            queries.append(('? {} {}'.format(a, b), resp1))
            fle = 0

        # 对应原来的：print('? a+2^(m-1-i), b+2^(m-1-i)'); resp2 = int(raw_input())
        x = a + (1 << (m - 1 - i))
        y = b + (1 << (m - 1 - i))
        resp2 = judge(x, y)
        queries.append(('? {} {}'.format(x, y), resp2))

        if resp1 == -1 and resp2 == 1:
            b += 1 << (m - 1 - i)
            fle = 1
        elif resp1 == 1 and resp2 == -1:
            a += 1 << (m - 1 - i)
            fle = 1

        else:
            fle = 0
            # 对应原来的：print('? a+2^(m-1-i), b'); resp3 = int(raw_input())
            x = a + (1 << (m - 1 - i))
            y = b
            resp3 = judge(x, y)
            queries.append(('? {} {}'.format(x, y), resp3))

            if resp3 == -1:
                b += 1 << (m - 1 - i)
                a += 1 << (m - 1 - i)

        # 更新 resp1 供下一轮使用
        # 在原交互题中，resp1 是上一轮对 (a, b) 的比较结果，
        # 这里我们按照逻辑重算一次，以保证一致性。
        resp1 = judge(a, b)

    # 对应原来的：print('! a b')
    result = (a, b)

    # 返回结果与测试数据，方便调用者验证
    return {
        "guessed_a": a,
        "guessed_b": b,
        "real_A": A,
        "real_B": B,
        "queries": queries,
    }


if __name__ == "__main__":
    # 示例调用：规模 n = 30
    info = main(30)
    # print("Guessed (a, b):", info["guessed_a"], info["guessed_b"])
    pass
    # print("Real    (A, B):", info["real_A"], info["real_B"])
    pass