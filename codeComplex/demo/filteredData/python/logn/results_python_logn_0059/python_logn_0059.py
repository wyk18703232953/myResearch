def main(n: int):
    # 生成测试数据：保证 l <= r，范围随 n 增大
    # 这里示例为：0 <= l <= r < 2^n
    if n <= 0:
        l, r = 0, 0

    else:
        # 简单构造：l 为 2^(n-1)，r 为 2^n - 1
        # 即最高位为 1，后面全是 1，覆盖一个典型区间
        l = 1 << (n - 1)
        r = (1 << n) - 1

    # 以下为原逻辑的无 input 版本
    a = bin(l)
    b = bin(r)
    a = "0" * (len(b) - len(a)) + a[2:len(a)]
    b = b[2:len(b)]
    c = [0 for _ in range(len(a))]
    flag = False
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = True
        if flag:
            c[i] = 1
    ans = 0
    for j in range(len(a)):
        ans += c[len(a) - 1 - j] * (2 ** j)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(5)