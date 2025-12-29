def check(n, p):
    k = str(n)[::-1]
    s = 0
    for j in range(len(k)):
        s += int(k[j]) * (10 ** j - 1)
    return 1 if s >= p else 0


def main(n):
    """
    n: 规模参数，用来生成测试数据和控制二分上界。
    测试数据生成规则（示例）：
    - 将原程序中的 p (这里变量名为 s) 设为 n // 2
    """
    s = n // 2  # 根据 n 生成示例测试数据

    l = 1
    h = n
    k = 0
    while l <= h:
        m = (l + h) // 2
        if check(m, s) == 0:
            l = m + 1
        else:
            h = m - 1
        k += 1

    # 保持原程序的输出行为：输出 n - l + 1
    print(n - l + 1)


if __name__ == "__main__":
    # 示例：调用 main(100) 进行测试
    main(100)