import random

def main(n: int):
    # 生成测试数据：n 行，每行若干整数
    # 保证第一行存在且非空
    data = []
    for i in range(n):
        # 每行长度随机为 1~5
        row_len = random.randint(1, 5)
        # 每个元素为 -10~10 的随机整数
        row = [random.randint(-10, 10) for _ in range(row_len)]
        data.append(row)

    # 原始逻辑开始
    a = []
    for i in range(n):
        l = data[i]
        if i == 0:
            t = sum(l)
        a.append(sum(l))
    a.sort(reverse=True)
    result = a.index(t) + 1

    # 输出结果
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)