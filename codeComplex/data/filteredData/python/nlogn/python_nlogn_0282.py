import random

def main(n: int):
    # 生成测试数据：
    # 使用 n 作为第一段数据规模，第二段规模设为 n（也可以按需要调整）
    m = n

    d = {}

    # 第一段数据：n 行 (a, x)
    # a 在 1..n 范围内随机生成，x 在 1..100 范围内随机生成
    for _ in range(n):
        a = random.randint(1, n)
        x = random.randint(1, 100)
        if a in d:
            d[a][0] += 1
            d[a][1].append(x)
        else:
            d[a] = [1, [x]]

    # 第二段数据：m 行 (a, x)
    for _ in range(m):
        a = random.randint(1, n)
        x = random.randint(1, 100)
        if a in d:
            d[a][0] += 1
            d[a][1].append(x)
        else:
            d[a] = [1, [x]]

    s = 0
    for key in d:
        count, values = d[key]
        if count == 1:
            s += values[0]
        else:
            s += max(values)

    print(s)


if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(10)