import random

def main(n):
    # 1. 生成规模为 n 的测试数据：n 个非负整数，范围可自行调整
    # 为了可复现，这里固定随机种子；如不需要可移除下一行
    random.seed(0)
    m = [random.randint(0, 10) for _ in range(n)]

    # 2. 保留原逻辑
    j = 0
    mark = [1]
    for i in range(1, len(m)):
        tmp = max(mark[i - 1], m[i] + 1)
        mark.append(tmp)

    j += mark[len(m) - 1] - m[len(m) - 1] - 1
    for i in range(len(m) - 2, -1, -1):
        if mark[i] < mark[i + 1] - 1:
            mark[i] = mark[i + 1] - 1
        j += mark[i] - m[i] - 1

    print(j)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)