import random

def main(n):
    # 生成测试数据：规模为 n 的数组 a，以及 k（不同数的个数目标）
    # 数组元素取值范围 1..n（可根据需要调整）
    a = [random.randint(1, n) for _ in range(n)]
    # k 取 1..n 之间的随机值（也可固定、可作为参数传入）
    k = random.randint(1, n)

    i = 0
    d = 0
    x = -1
    y = -1
    MAXV = 10**5 + 1
    s = [0] * MAXV

    for j in range(len(a)):
        val = a[j]
        if val >= MAXV:
            # 简单防御：若生成数据超出计数数组范围，可扩展或限制生成范围
            continue
        s[val] += 1
        i += 1
        if s[val] == 1:
            d += 1
        if i == 1:
            x = j + 1
        if d == k:
            y = j + 1
            break

    while k != 1 and x != -1 and s[a[x - 1]] - 1 != 0:
        s[a[x - 1]] -= 1
        x += 1

    if x == -1 or y == -1:
        x = -1
        y = -1

    print(x, y)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)