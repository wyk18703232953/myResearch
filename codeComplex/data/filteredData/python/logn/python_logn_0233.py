def main(n):
    # 生成测试数据：随机选择一个合理的 s（1 <= s <= n 或稍小）
    # 这里简单设为 n // 2，若需随机可改用 random
    s = max(1, n // 2)

    if n <= s:
        print(0)
        return

    for i in range(s, n + 2):
        digit_sum = sum(int(d) for d in str(i))
        if i - digit_sum >= s:
            break

    print(max(n - i + 1, 0))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(100000)