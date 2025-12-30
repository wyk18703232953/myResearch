import random

def main(n):
    # 生成测试数据：
    # 使用 n 作为第一组数据的条数，同时生成第二组数据条数 m（可与 n 相同）
    m = n

    d = {}

    # 第一组：生成 n 对 (a, x)
    # a 使用较大的取值范围避免过多冲突
    for _ in range(n):
        a = random.randint(1, 10 * n + 10)
        x = random.randint(0, 100)
        d[a] = x

    # 第二组：生成 m 对 (b, y)
    for _ in range(m):
        b = random.randint(1, 10 * n + 10)
        y = random.randint(0, 100)
        if b in d:
            d[b] = max(y, d[b])
        else:
            d[b] = y

    count = 0
    for v in d.values():
        count += v

    print(count)


if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改或在外部调用 main(n)
    main(10)