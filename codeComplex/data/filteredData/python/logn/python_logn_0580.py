def main(n):
    # 生成测试数据：k 的规模随 n 增长，这里简单取为 10**n
    # 可根据需要调整为其它与 n 相关的值
    k = 10 ** n

    n = 1
    up_bnd = 9
    while k > up_bnd:
        n += 1
        up_bnd += (9 * n) * (10 ** (n - 1))

    low_bnd = 0
    lb_val = 0
    for i in range(1, n):
        low_bnd += (9 * i) * (10 ** (i - 1))
        lb_val = (lb_val * 10) + 9

    num = int((k - low_bnd) / n) + lb_val
    rm = (k - low_bnd) % n

    if rm != 0:
        num += 1

    if rm == 0:
        ans = num % 10
    else:
        ans = 0
        for _ in range(n - rm + 1):
            j = num % 10
            num = int(num / 10)
            ans = j

    print(int(ans))


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)