import random

def main(n):
    # 生成测试数据：
    # n 为第一次读入的对数
    # m 为第二次读入的对数，这里设为 n，规模同级
    # 索引和值都在 1..10^6 范围内随机生成
    m = n

    # 用于模拟原始逻辑的“输入数据”
    first_pairs = []
    for _ in range(n):
        indx = random.randint(1, 10**6)
        y = random.randint(1, 10**6)
        first_pairs.append((indx, y))

    second_pairs = []
    for _ in range(m):
        indx = random.randint(1, 10**6)
        y = random.randint(1, 10**6)
        second_pairs.append((indx, y))

    # 原始逻辑开始
    d = {}
    sm = 0

    # 处理第一批 n 组 (indx, y)
    for indx, y in first_pairs:
        d[indx] = [1, [y]]

    # 处理第二批 m 组 (indx, y)
    for indx, y in second_pairs:
        if indx in d:
            d[indx][0] += 1
            d[indx][1].append(y)
        else:
            d[indx] = [1, [y]]

    # 计算结果
    for key in d:
        count, values = d[key]
        if count == 1:
            sm += values[0]
        else:
            sm += max(values)

    print(sm)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)