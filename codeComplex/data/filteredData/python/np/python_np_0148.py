import random

def main(n: int):
    # 1. 生成测试数据：随机生成 n 个区间 [l[i], r[i]]
    # 为保证逻辑正常，这里让区间长度适中，值域不超过 10000
    # 你可以根据需要修改生成规则
    l = []
    r = []
    for _ in range(n):
        a = random.randint(0, 9000)
        b = random.randint(a, min(a + random.randint(0, 1000), 9999))
        l.append(a)
        r.append(b)

    # 2. 原程序逻辑
    big = 1
    for i in range(n):
        big *= (r[i] - l[i] + 1)

    out = 0

    # 第一部分
    for amt in range(10000):
        for x in range(n):
            for y in range(n):
                if x == y:
                    continue
                local = big
                for i in range(n):
                    if i == x:
                        if amt < l[i] or amt > r[i]:
                            local = 0
                        local //= (r[i] - l[i] + 1)
                    elif i == y:
                        if amt > r[i]:
                            local = 0
                        range_size = r[i] - amt + 1
                        range_size -= 1
                        local //= (r[i] - l[i] + 1)
                        local *= min(r[i] - l[i] + 1, range_size)
                    else:
                        if amt < l[i]:
                            local = 0
                        range_size = amt - l[i] + 1
                        if i > x:
                            range_size -= 1
                        local //= (r[i] - l[i] + 1)
                        local *= min(r[i] - l[i] + 1, range_size)
                out += amt * local

    # 第二部分
    for amt in range(10000):
        for x in range(n):
            for y in range(n):
                if x >= y:
                    continue
                local = big
                for i in range(n):
                    if i == x:
                        if amt < l[i] or amt > r[i]:
                            local = 0
                        local //= (r[i] - l[i] + 1)
                    elif i == y:
                        if amt > r[i] or amt < l[i]:
                            local = 0
                        local //= (r[i] - l[i] + 1)
                    else:
                        if amt < l[i]:
                            local = 0
                        range_size = amt - l[i] + 1
                        if i > x:
                            range_size -= 1
                        local //= (r[i] - l[i] + 1)
                        local *= min(r[i] - l[i] + 1, range_size)
                out += amt * local

    if out == 666716566686665150040000:
        print("6667.1666666646")
    else:
        print('%.12f' % (out / big))


if __name__ == "__main__":
    # 示例：调用 main(n)，这里给一个默认值，你可以自行修改或从外部调用 main
    main(3)