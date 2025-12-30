def main(n):
    import random

    # 生成测试数据
    # n: 查询次数规模
    # 约束：0 <= c <= 255, 1 <= k <= 256
    k = random.randint(1, 256)
    queries = [random.randint(0, 255) for _ in range(n)]

    a = [0 for _ in range(256)]
    outputs = []

    for c in queries:
        if a[c] != 0:
            outputs.append(str(a[c] - 1))
        else:
            # 向左寻找可用区间起点
            i = 0
            for x in range(c, c - k, -1):
                if a[x] == 0:
                    i = x
                else:
                    if c - a[x] + 1 < k:
                        i = a[x] - 1
                    break
                if x == 0:
                    break
            # 填充区间
            for x in range(int(i), c + 1):
                a[x] = i + 1
            outputs.append(str(i))

    # 按原逻辑输出（用空格分隔，末尾无多余空格）
    print(" ".join(outputs))


if __name__ == "__main__":
    # 示例：规模为10
    main(10)