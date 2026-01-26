def main(n):
    curpow, t, mx2pow = 1, 1, 0
    while t < n:
        t <<= 1
        mx2pow += 1

    if t > n:
        mx2pow -= 1

    last = 1 << (mx2pow - 1) if mx2pow else 1
    add = last

    while last < n:
        last += add

    if last > n:
        last -= add

    while n:
        if n == 1:
            # print(last)
            pass
            break
        # print((str(curpow) + ' ') * ((n + 1) // 2), end='')
        pass
        curpow *= 2
        n //= 2


if __name__ == "__main__":
    # 这里根据规模 n 生成测试数据，直接使用 n 作为参数调用 main
    # 可按需要修改测试的 n 值
    test_n = 10
    main(test_n)