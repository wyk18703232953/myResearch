def main(n: int):
    # n 作为原程序中的 k 使用
    k = n
    k_ = k
    ca = 9
    di = 1
    tem = 9
    while k_ > 0:
        k_ -= ca * di
        ca *= 10
        di += 1
        tem += ca * di
        if k_ == 0:
            break
    tem -= ca * di
    ca = int(ca / 10)
    di -= 1
    tem -= ca * di
    ca = int(ca / 10)
    ca_ = 0
    while ca > 0:
        ca_ += ca
        ca = int(ca / 10)
    k -= tem
    re = int((k + di - 1) // di) + ca_
    re_ = k % di
    if re_ == 0:
        l = 1
    else:
        l = 10 ** (di - re_)
    re = int(re // l)
    print(re % 10)


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据
    # 这里直接用 n 作为原程序的 k
    test_n = 1000
    main(test_n)