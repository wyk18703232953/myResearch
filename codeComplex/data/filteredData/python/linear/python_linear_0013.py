def main(n):
    # 根据 n 生成测试数据，这里设定 k 为 n // 4（可按需调整生成策略）
    k = n // 4

    # 原逻辑开始：筛出素数列表 v
    v = []
    for i in range(2, n + 1):
        if all(i % j != 0 for j in v):
            v.append(i)

    # 统计满足条件的素数三元组个数
    c = 0
    for i in range(len(v) - 1):
        if 1 + v[i] + v[i + 1] in v:
            c += 1

    # 输出结果
    if c >= k:
        print("YES")
    else:
        print("NO")


# 示例调用
if __name__ == "__main__":
    main(50)