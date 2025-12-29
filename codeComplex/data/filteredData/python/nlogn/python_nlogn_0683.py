import random

def main(n):
    # 生成测试数据：
    # boys 数组长度为 n，girls 数组长度 m 可以与 n 相同或不同，这里设为 n 或 n+1 随机
    m = n + random.randint(0, 1)  # 保证 m >= n 的常见情形，也可能 m == n
    # 随机生成男孩和女孩的能力值，正整数
    boys = [random.randint(1, 10) for _ in range(n)]
    girls = [random.randint(1, 10) for _ in range(m)]

    # 以下为原始逻辑
    boys.sort(reverse=True)
    girls.sort(reverse=True)
    s = sum(boys)
    ma = max(boys)
    res = 0

    for i in range(0, m):
        if girls[i] < ma:
            print(-1)
            return
        res += s
        if girls[i] == ma:
            girls[i] = 0

    j = 0
    usage = 0
    for i in range(0, m):
        if usage == m - 1:
            j += 1
        if j >= n:
            print(-1)
            return
        res += max(0, girls[i] - boys[j])
        usage += 1

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)