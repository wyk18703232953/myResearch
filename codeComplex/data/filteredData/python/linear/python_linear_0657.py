import random

def main(n: int):
    # 1. 生成测试数据
    # 生成一个随机树：n 个节点，n-1 条边
    # s 随机生成为 1~1000 范围内的整数（可根据需要调整）
    s = random.randint(1, 1000)

    # 构造一棵随机树：对于 i=2..n，随机连到 [1, i-1] 的某个节点
    edges = []
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        edges.append((parent, i))

    # 2. 按原逻辑处理
    d = [0] * (n + 1)
    cnt = 0

    for a, b in edges:
        d[a - 1] += 1
        d[b - 1] += 1

    for i in range(0, n):
        if d[i] == 1:
            cnt += 1

    # 3. 输出结果（对应原程序的 print）
    if cnt == 0:
        print("No leaf nodes, division by zero avoided.")
    else:
        print(2.0 * s / cnt)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此修改
    main(10)