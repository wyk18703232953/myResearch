def pow2(n):
    j = 0
    while n % 2 == 0:
        n //= 2
        j += 1
    return j


def main(n):
    # 生成测试数据：
    # 设查询次数 q = n
    # 对每个查询：
    #   u 为 [1, n] 内的一个数（这里简单按循环取值）
    #   s 为由 'L', 'R', 'U' 组成的操作串，长度与 n 相关（例如 min(10, n)）
    q = n
    max_len = min(10, n)
    ops = ['L', 'R', 'U']

    results = []

    for j in range(q):
        # 生成 u：在 1..n 范围内循环
        u = (j % n) + 1

        # 生成操作串 s：循环使用 L, R, U
        s = ''.join(ops[(j + k) % 3] for k in range(max_len))

        # 原始逻辑
        for k in range(len(s)):
            num = pow2(u)
            if s[k] == "R" and num != 0:
                u = u + 2 ** (num - 1)
            elif s[k] == "L" and num != 0:
                u = u - 2 ** (num - 1)
            elif s[k] == "U" and u != (n + 1) // 2:
                m1 = u + 2 ** num
                m2 = u - 2 ** num
                if pow2(m1) == (num + 1):
                    u = m1
                else:
                    u = m2

        results.append(u)

    # 输出结果
    for val in results:
        print(val)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)