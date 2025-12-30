import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据 g
    # 这里生成一个 1 到 100 之间的随机整数序列
    t = n
    g = [random.randint(1, 100) for _ in range(t)]

    # 2. 以下是原逻辑的改写（去掉 input/exit，封装成 main）
    k = max(g)
    i = 0

    # 单峰上升部分（直到第一个最大值）
    while i < t and g[i] != k:
        if i != 0 and g[i] < g[i - 1]:
            print("NO")
            return
        i += 1

    # 跳过第一个最大值
    i += 1

    # 单峰下降部分（从第一个最大值之后继续，直到下一个最大值或结束）
    while i < t and g[i] != k:
        if i != 0 and g[i] > g[i - 1]:
            print("NO")
            return
        i += 1

    print("YES")


if __name__ == "__main__":
    # 示例调用：n 为序列长度
    main(10)