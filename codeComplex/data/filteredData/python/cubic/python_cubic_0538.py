def main(n: int):
    """
    规模 n 用来控制生成的整数 b 的位数。
    测试数据生成规则：
      - 生成一个 n 位的整数 b（最高位不为0）
      - 将 b 转成字符串作为 a 的来源（打乱并排序后再逆序）
    返回：程序最终输出的字符串 p
    """

    import random

    # 1. 生成测试数据：b 是一个 n 位整数
    if n <= 0:
        return ""

    # 确保最高位非 0
    first_digit = random.randint(1, 9)
    other_digits = [random.randint(0, 9) for _ in range(n - 1)]
    digits = [str(first_digit)] + [str(d) for d in other_digits]
    b_str = "".join(digits)
    b = int(b_str)

    # 2. 原始逻辑开始
    # a 来自 b 的数字 multiset；原程序是从 input() 读字符串，这里用 b_str 的数字乱序生成
    a_list = list(b_str)
    random.shuffle(a_list)
    a = sorted(a_list)         # 与原程序等价：a = sorted(input())
    a = a[::-1]                # reverse a

    p = ''
    cnt = [0] * 10  # 原代码未使用，仅保留

    while a:
        for i, d in enumerate(a):
            # 尝试将当前字符 d 放到 p 后面，然后剩余字符按升序放在末尾
            n_candidate = p + d + "".join(sorted(a[:i] + a[i + 1:]))
            if int(n_candidate) <= b:
                p += d
                a.pop(i)
                break

    # 输出结果
    print(p)
    return p


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)