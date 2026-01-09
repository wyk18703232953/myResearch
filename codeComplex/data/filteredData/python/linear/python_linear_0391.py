def main(n):
    p = 998244353
    # 生成确定性的输入结构：
    # 原程序：n 行，每行若干整数 -> 被 readline() 转成 map(int, ...)
    # 之后 a = list(readline())，并使用下标和整数运算，
    # 所以这里构造一个长度为 n 的整数列表
    # 例：a[i] = (i + 1) % p
    a = [(i + 1) % p for i in range(n)]
    if n == 0:
        return 0
    answer = a[-1]
    pow_ = 1
    for i in range(n - 1, 0, -1):
        answer = (answer + a[i - 1] * (2 + n - i) * pow_ % p) % p
        pow_ = pow_ * 2 % p
    return answer


if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模运行
    # print(main(10))
    pass