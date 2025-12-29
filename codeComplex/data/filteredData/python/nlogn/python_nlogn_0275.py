import random

def main(n):
    # 生成测试数据：n 对 (a, b)
    # a, b 范围可自行调整，这里设为 [1, n]
    pairs = []
    for i in range(n):
        a = random.randint(1, n)
        b = random.randint(1, n)
        pairs.append([a, b, i])  # 第三个元素存原始下标

    # 以下为原逻辑
    pairs.sort(key=lambda x: (x[0], -x[1]))
    for i in range(1, n):
        if pairs[i][1] <= pairs[i - 1][1]:
            print(pairs[i][2] + 1, pairs[i - 1][2] + 1)
            break
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)