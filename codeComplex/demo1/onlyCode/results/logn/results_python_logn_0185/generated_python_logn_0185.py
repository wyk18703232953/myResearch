def main(n):
    # 依据原程序含义需要一个下界 s，这里用简单的测试数据生成方式：
    # 让 s = n // 2（你可以根据需要修改生成规则）
    s = n // 2

    lo, hi = s, n
    ans = n + 1
    while lo <= hi:
        mid = (lo + hi) // 2
        z = sum(map(int, str(mid)))
        if mid >= s + z:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(n - ans + 1)


if __name__ == "__main__":
    # 示例：使用规模 n=10 运行
    main(10)