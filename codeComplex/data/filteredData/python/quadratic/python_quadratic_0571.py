from sys import stdout

def main(n):
    # 这里根据 n 生成测试数据 (n, m)
    # 示例策略：让 m = n（你可以按需求修改）
    m = n

    if n == 2:
        c = 1
        way = []
        mult = 1
        for x in range(m - 1, -1, -1):
            way.append(c)
            c += x * mult
            mult *= -1
        for x in way:
            print(1, x)
        for x in way[::-1]:
            print(2, x)

    elif n == 1:
        c = 1
        way = []
        mult = 1
        for x in range(m - 1, -1, -1):
            way.append(c)
            c += x * mult
            mult *= -1
        for x in way:
            print(1, x)

    elif m == 2:
        c = 1
        way = []
        mult = 1
        for x in range(n - 1, -1, -1):
            way.append(c)
            c += x * mult
            mult *= -1
        for x in way:
            print(x, 1)
        for x in way[:-1:-1]:
            print(x, 2)

    elif m == 1:
        c = 1
        way = []
        mult = 1
        for x in range(n - 1, -1, -1):
            way.append(c)
            c += x * mult
            mult *= -1
        for x in way:
            print(x, 1)

    else:
        for x in range(n // 2):
            for y in range(1, m + 1):
                stdout.write(str(x + 1) + ' ' + str(y) + '\n')
                stdout.write(str(n - x) + ' ' + str(m + 1 - y) + '\n')
        if n % 2 == 1:
            c = 1
            way = []
            mult = 1
            for x in range(m - 1, -1, -1):
                way.append(c)
                c += x * mult
                mult *= -1
            for x in way:
                stdout.write(str(n // 2 + 1) + ' ' + str(x) + '\n')


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的具体值
    main(5)