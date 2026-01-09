def main(n):
    if n <= 0:
        return

    # 确定性生成输入数据
    # 原始结构：第一行是 n，第二行是包含 n 个整数的数组 ar
    # 这里将 ar 构造为一个含有正负混合的序列，便于覆盖不同分支：
    #   前 1/3 为负数，中间 1/3 为 0，后 1/3 为正数
    ar = []
    for i in range(n):
        if i % 3 == 0:
            ar.append(-i - 1)
        elif i % 3 == 1:
            ar.append(0)

        else:
            ar.append(i + 1)

    # 核心算法逻辑保持不变
    if n == 1:
        # print(ar[0])
        pass
        return

    onlyNegs = True
    onlyPos = True

    if max(ar) >= 0:
        onlyNegs = False
    if min(ar) <= 0:
        onlyPos = False

    if onlyNegs:
        # print(abs(sum(ar)) + max(ar) * 2)
        pass
        return

    if onlyPos:
        # print(abs(sum(ar)) - min(ar) * 2)
        pass
        return

    # print(sum(abs(i) for i in ar))
    pass
if __name__ == "__main__":
    main(10)