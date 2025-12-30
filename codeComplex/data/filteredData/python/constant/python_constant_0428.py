def main(n):
    # 根据 n 生成测试数据，这里示例：令 k = 2 * n + 1（可按需要调整生成规则）
    k = 2 * n + 1

    if n >= k:
        return (k - 1) // 2
    elif n * 2 > k:
        return n - k // 2
    else:
        return 0


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可由外部代码调用 main(n)
    result = main(10)
    print(result)