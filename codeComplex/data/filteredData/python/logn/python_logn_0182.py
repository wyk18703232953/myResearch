def main(n: int):
    # 生成测试数据 m，规模随 n 变化：
    # 这里示例为 m = n // 2，可根据需要调整生成规则
    m = n // 2

    be, en, ans = 1, n, n + 1
    while be <= en:
        md = (be + en) >> 1
        if md - sum(int(x) for x in str(md)) >= m:
            en = md - 1
            ans = md
        else:
            be = md + 1

    # 输出结果
    print(n - ans + 1)


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10**6)