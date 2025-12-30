def main(n: int):
    # 根据规模 n 生成测试数据：这里假设 m 为 n 的一半（也可以按需调整生成方式）
    m = n // 2

    be, en, ans = 1, n, n + 1
    while be <= en:
        md = (be + en) >> 1
        if md - sum(int(x) for x in str(md)) >= m:
            en = md - 1
            ans = md
        else:
            be = md + 1

    print(n - ans + 1)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(10**6)