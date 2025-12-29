# http://codeforces.com/contest/992/problem/C

def main(n):
    """
    n: 生成测试数据的规模，这里用来构造 (x, k)
       约定：
       - x = n
       - k = n
       若需其他数据分布，可在此处调整生成规则。
    """
    # 生成测试数据
    x = n
    k = n

    md = 10 ** 9 + 7

    if x > 0:
        res = x * pow(2, k + 1, md) - pow(2, k, md) + 1
    else:
        res = 0

    res %= md
    print(res)


if __name__ == "__main__":
    # 示例：可以在此处手动指定n来运行
    # 如需批量测试，可自行循环调用 main(n)
    main(5)