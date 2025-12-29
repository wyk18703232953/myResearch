import random

def main(n):
    # 生成测试数据：
    # n: r 数量
    # m: d 数量
    # 这里令 m = max(1, n // 2)，可按需修改生成规则
    m = max(1, n // 2)

    # 生成 r 和 d 的值（保证整体长度为 n + m，且恰好含 n 个 0 和 m 个 1 的 t）
    # 随机生成 n+m 个数作为 x
    total_len = n + m
    x = [random.randint(1, 1000) for _ in range(total_len)]

    # 生成 t，使得有 m 个 1，n 个 0
    t = [0] * n + [1] * m
    random.shuffle(t)

    # 以下为原逻辑，只是用生成的 x,t,n,m 进行计算
    r = [0] * n
    d = [0] * m
    countr = 0
    countd = 0

    for i in range(n + m):
        if int(t[i]) == 1:
            d[countd] = int(x[i])
            countd += 1
        else:
            r[countr] = int(x[i])
            countr += 1

    current = 0
    count = [0] * m
    for i in range(n):
        while current < m - 1:
            if d[current + 1] >= r[i]:
                break
            current += 1
        if current == m - 1:
            count[m - 1] += (n - i)
            break
        if 2 * r[i] <= (d[current] + d[current + 1]):
            count[current] += 1
        else:
            count[current + 1] += 1

    # 输出结果
    s = ""
    for i in range(m):
        s += str(count[i]) + " "
    print(s[:-1])

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)