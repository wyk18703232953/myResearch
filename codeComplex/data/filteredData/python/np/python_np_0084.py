def factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

def n_choose_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def solve(diff, u):
    pluses = u + 1
    n = 2 ** u
    for i in range(u, -u - 1, -2):
        pluses -= 1
        if diff == i:
            k = n_choose_k(u, pluses)
            return k / n
    return 0.0

def main(n):
    """
    n: 规模参数，用来生成测试数据。
       此处我们生成：
       - s1: 长度为 n，由'+'和'-'随机组成（这里做一个确定性构造）
       - s2: 长度为 n，由'+', '-', '?' 组成（同样做确定性构造）
       
    可根据需要修改数据生成方式。
    """
    # 简单确定性测试数据生成：
    # s1: 前半部分 '+', 后半部分 '-'
    half = n // 2
    s1 = '+' * half + '-' * (n - half)

    # s2: 前 1/3 用 '+', 中间 1/3 用 '-', 剩余用 '?'
    third = n // 3
    s2 = '+' * third + '-' * third + '?' * (n - 2 * third)

    correct_p = 0
    pred_p = 0
    unknown = 0

    for c in s1:
        correct_p += 1 if c == '+' else -1

    for c in s2:
        if c in '+-':
            pred_p += 1 if c == '+' else -1

        else:
            unknown += 1

    if unknown == 0 and correct_p == pred_p:
        p = 1.0

    else:
        p = solve(correct_p - pred_p, unknown)

    # print('{0:.9f}'.format(p))
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)