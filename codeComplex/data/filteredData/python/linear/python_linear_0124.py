import random

def main(n: int):
    # 生成测试数据：构造一个长度为 n-1 的序列，每个元素在 [1, n] 范围内
    # 保持与原代码语义：l[2..n] 存储读入的 n-1 个数
    d = [0] * (n + 1)
    l = [0] * 2
    m = [0] * (n + 1)

    # 生成 n-1 个随机整数，范围 [1, n]
    edges = [random.randint(1, n) for _ in range(n - 1)]

    for a in edges:
        l.append(a)
        m[a] += 1

    for i in range(1, n + 1):
        if m[i] == 0:
            # 注意：原代码里直接使用 d[l[i]]，这里保持一致
            d[l[i]] += 1

    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)