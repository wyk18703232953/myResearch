def main(n):
    # 根据 n 生成测试数据：
    # 这里随机构造 m, a, b 的一种示例方式（可按需要调整生成规则）
    # 确保 m > 0 且与 n 有合理关系
    m = max(1, n * 2)       # 示例：令 m 为 2n，保证 m > 0
    a = n + 1               # 示例：a 与 n 正相关
    b = n * 2 + 3           # 示例：b 与 n 正相关但不同

    # 原逻辑：给定 n, m, a, b，输出：
    # min(n % m * b, (m - n % m) * a)
    res = min(n % m * b, (m - n % m) * a)
    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)