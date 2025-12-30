def main(n: int):
    # 自动生成测试数据：v 的范围为 [1, n]
    # 这里选择 v = max(1, min(n, n // 2)) 作为示例，可根据需要调整生成策略
    v = max(1, min(n, n // 2))

    ans = min(v, n - 1)
    for i in range(n - v - 1):
        ans += i + 2
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可在外部以不同 n 调用 main
    main(10)