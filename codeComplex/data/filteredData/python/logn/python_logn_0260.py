def bpow(base, exp, md):
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return (base * bpow(base, exp - 1, md)) % md

    else:
        k = bpow(base, exp // 2, md)
        return (k * k) % md


def main(n):
    """
    n 为规模参数，这里用来生成测试数据 (x, k)。
    你可以根据需要修改生成策略。
    当前策略：
        x = n
        k = n + 1
    """
    md = 1000000007
    x = n
    k = n + 1

    pw = bpow(2, k, md)
    ans = (2 * pw * x) % md
    if x != 0:
        ans -= pw - 1
    ans = (ans + md) % md
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)