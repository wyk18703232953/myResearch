def main(n):
    # 生成测试数据：随机生成一个合理范围内的 s（1 <= s <= n）
    # 这里简单起见，用中点作为测试数据，也可改为其它策略
    s = max(1, n // 2)

    l = n + 1
    upper = min(s + 1000000, n)
    for i in range(s, upper + 1):
        cur = sum(int(j) for j in str(i))
        if i - cur >= s:
            l = i
            break
    result = n - l + 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要调整或由外部调用传参
    main(10**6)