def main(n):
    # 根据规模 n 生成测试数据：这里生成 k，保证有一定变化
    # 你可以根据需要修改生成规则
    k = 2 * n + 1  # 示例规则：k = 2n + 1

    if n >= k:
        ans = (k - 1) // 2
    elif n * 2 > k:
        ans = n - k // 2

    else:
        ans = 0

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)