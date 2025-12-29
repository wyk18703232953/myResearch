def main(n):
    # 根据 n 生成测试数据：k 为 1 到 n*(n+1)//2 之间的某个值
    # 这里只是一个示例策略：令 k 为中间值
    max_k = n * (n + 1) // 2
    k = max_k // 2 if max_k > 0 else 0

    c = 1
    # 第一段 while：找到满足 c*(c+1)//2 >= k 的最小 c
    while c * (c + 1) // 2 < k:
        c += 1
    # 第二段 while：再调整 c 直至满足给定关系式
    while c * (c + 1) // 2 - (n - c) != k:
        c += 1

    # 输出结果
    print(n - c)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需要调整
    main(10)