def main(n):
    """
    使用原算法逻辑，对从 1 开始连续拼接的数字串（"123456789101112..."）中，
    找到第 k 位上的数字。这里的 k 由规模 n 自动生成测试数据。
    """
    # 生成测试数据：根据规模 n 生成一个适中的 k
    # 这里生成一个大约在 [10^(n-1), 10^n) 范围内的 k，用于测试
    if n <= 0:
        return
    k = 10 ** (n - 1) + (10 ** (n - 1)) // 2  # 可以按需调整生成规则

    # 以下为原逻辑，去掉 input()，直接使用 k
    n_digit = 1
    up_bnd = 9
    while k > up_bnd:
        n_digit += 1
        up_bnd += (9 * n_digit) * (10 ** (n_digit - 1))

    low_bnd = 0
    for i in range(1, n_digit):
        low_bnd += (9 * i) * (10 ** (i - 1))

    num = (k - low_bnd) // n_digit

    lb_val = 0
    for _ in range(n_digit - 1):
        lb_val = (lb_val * 10) + 9

    num += lb_val
    rm = (k - low_bnd) % n_digit

    if rm != 0:
        num += 1

    ans = 0
    if rm == 0:
        ans = num % 10

    else:
        for _ in range(n_digit - rm + 1):
            j = num % 10
            num //= 10
            ans = j

    # print(int(ans))
    pass
if __name__ == "__main__":
    # 示例：调用 main(3) 作为测试
    main(3)