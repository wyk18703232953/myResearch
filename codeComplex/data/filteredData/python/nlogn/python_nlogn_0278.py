import random

def main(n):
    # 生成测试数据：
    # 使用 n 作为键值对的数量规模
    # 第一组：n 对 (a, b)
    # 第二组：m 对 (a, b)，这里令 m = n
    d = {}

    # 生成第一组数据：n 对 (a, b)
    # a 尽量不重复以体现插入操作，b 为正整数
    for _ in range(n):
        a = random.randint(1, n * 2)
        b = random.randint(1, 100)
        d[a] = b

    # 生成第二组数据：m = n，对同一键可能出现更大或更小的值
    for _ in range(n):
        a = random.randint(1, n * 2)
        b = random.randint(1, 100)
        if d.get(a) is None:
            d[a] = b
        else:
            if b > d[a]:
                d[a] = b

    ans = 0
    for key in d:
        ans += d[key]
    print(ans)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)