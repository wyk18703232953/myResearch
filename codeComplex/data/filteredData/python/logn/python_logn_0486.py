def main(n: int):
    """
    n 作为规模参数，这里用来生成测试数据：
    令 k = n，对应原程序中单次查询的 k。
    原程序中 q 固定为 1，这里同样只处理一次。
    """
    k = max(1, int(n))  # 保证 k 为正整数

    m = 0
    p = 9
    while k > p:
        m = m + 1
        l = p
        p = p + 9 * (10 ** m) * (m + 1)

    if m == 0:
        print(k)
        return

    ans = int("9" * m) + (k - l) // (m + 1)
    if (k - l) % (m + 1) == 0:
        print(str(ans)[-1])
    else:
        ans = ans + 1
        print(str(ans)[((k - l) % (m + 1)) - 1])


if __name__ == "__main__":
    # 示例：调用 main(15)
    main(15)