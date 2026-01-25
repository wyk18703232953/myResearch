def main(n):
    # n 控制输入规模，这里用作两个等长二进制串的长度
    if n <= 0:
        print(0)
        return

    # 确定性构造两个“数字串” a_str, b_str，由数字 0/1 组成
    # 使用简单算术模式，完全由 n 决定
    a_str = ''.join(str((i // 2) % 2) for i in range(n))
    b_str = ''.join(str((i + 1) % 2) for i in range(n))

    a = [int(c) for c in a_str]
    b = [int(c) for c in b_str]

    b_len = len(b)
    a_len = len(a)

    carCountPrefix = [[0 for _ in range(2)] for _ in range(b_len + 1)]
    b_zero_count = 0
    b_one_count = 0
    for b_i in range(b_len):
        if b[b_i] == 0:
            b_zero_count += 1
        elif b[b_i] == 1:
            b_one_count += 1
        carCountPrefix[b_i + 1][1] = b_one_count
        carCountPrefix[b_i + 1][0] = b_zero_count

    res = 0
    for cur in range(0, a_len):
        for dig in range(2):
            res += (carCountPrefix[b_len - a_len + cur + 1][dig] - carCountPrefix[cur][dig]) * abs(a[cur] - dig)
    print(res)


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)