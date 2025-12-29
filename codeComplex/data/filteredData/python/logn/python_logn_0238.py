def main(n):
    # 根据 n 生成测试数据，这里简单设定 s 为 n 的一半（仅示例，可按需修改）
    s = n // 2

    mult_10 = s if not (s % 10) else s + 10 - (s % 10)
    low = mult_10 + 100000  # 默认一个大值，若找不到满足条件的 i，则结果为 0
    for i in range(mult_10, mult_10 + 100000, 10):
        if i - sum(int(c) for c in str(i)) >= s:
            low = i
            break

    ans = max(n - low + 1, 0)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10^9) 或其他规模
    main(10**6)