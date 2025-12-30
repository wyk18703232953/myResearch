import random

def main(n):
    # 生成测试数据
    # n: 条目个数
    # m: 随机设为 [n, 3n] 区间内的整数，防止太极端
    m = random.randint(n, 3 * n)
    data = []
    for _ in range(n):
        # 生成 a, b。a >= b 保证 a-b 非负（可根据需要调整）
        b = random.randint(0, 10)
        a = b + random.randint(0, 10)
        data.append((a, b))

    # 原算法逻辑
    l = []
    s1 = s2 = 0
    for a, b in data:
        s1 += a
        s2 += b
        l.append(a - b)

    if s1 <= m:
        print(0)
    elif s2 > m:
        print(-1)
    else:
        r = 0
        l.sort(reverse=True)
        for x in l:
            r += 1
            s1 -= x
            if s1 <= m:
                print(r)
                break


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)