def main(n):
    # 确定性生成测试数据
    # n 至少为 1
    if n <= 0:
        return
    # 设定 k，为不同元素个数目标：
    # 若 n >= 5，令 k 为 n//3，至少为 1 且不超过不同元素上限
    # 若 n < 5，则令 k = min(3, n)
    k = max(1, min(n // 3 if n >= 5 else 3, n))

    # 生成长度为 n 的数组 a，元素分布确定性：
    # 重复模式：i % max(1, k//2 + 1) 保证有一些重复
    base = max(1, k // 2 + 1)
    a = [(i % base) + 1 for i in range(n)]

    # 原算法逻辑开始
    count = 0
    b = {}
    i = -1
    for idx in range(n):
        if a[idx] in b:
            b[a[idx]] += 1

        else:
            b[a[idx]] = 1
        if b[a[idx]] == 1:
            count += 1
        if count == k:
            i = idx
            break

    for j in range(n):
        if a[j] in b:
            b[a[j]] -= 1
        if b.get(a[j], 0) == 0:
            break

    if count != k:
        # print("-1 -1")
        pass

    else:
        if n == 1:
            # print(1, 1)
            pass
        elif n == 2 and count == 2:
            # print(1, 2)
            pass

        else:
            # print(j + 1, i + 1)
            pass
if __name__ == "__main__":
    # 示例：可修改 n 进行规模化实验
    main(10)