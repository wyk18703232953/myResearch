def main(n: int):
    # 根据规模 n 生成测试数据，这里假设：
    # x = n，k = n
    x = n
    k = n

    mod = 1000 * 1000 * 1000 + 7
    if x == 0:
        # print(0)
        pass

    else:
        mul = pow(2, k + 1, mod)
        cnt = pow(2, k, mod)
        s1 = mul * cnt * x
        s2 = cnt * (cnt - 1)
        ans = (s1 - s2) % mod
        rev = pow(cnt, mod - 2, mod)
        assert rev * cnt % mod == 1
        ans *= rev
        # print(ans % mod)
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)