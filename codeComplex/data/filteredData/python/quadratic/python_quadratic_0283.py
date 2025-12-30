import random

def main(n):
    # 生成测试数据
    # 序列长度为 n，f 的长度取 n 的一半（至少为 1）
    m = max(1, n // 2)
    # seq 中元素范围 1~2n
    seq = [random.randint(1, 2 * n) for _ in range(n)]
    # f 中元素也从同一范围生成
    f = [random.randint(1, 2 * n) for _ in range(m)]

    # 原逻辑：找出 seq 中出现在 f 中的元素（保留顺序和重复）
    a = []
    for i in range(n):
        for j in range(m):
            if seq[i] == f[j]:
                a.append(seq[i])
                break  # 一旦匹配即可，不必继续在 f 中找

    # 输出结果
    for x in a:
        print(x, end=' ')


if __name__ == "__main__":
    # 示例：可修改 n 测试
    main(10)