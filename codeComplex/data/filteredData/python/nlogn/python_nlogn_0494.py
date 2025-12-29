import random

def main(n):
    # 生成测试数据
    # 随机生成 n 对 (a, b)，并生成预算 m
    # 保证 a, b 为非负整数，a >= b，方便模拟原逻辑中 a-b 的意义
    pairs = []
    o = 0  # 总 a
    c = 0  # 总 b
    for _ in range(n):
        b = random.randint(0, 100)
        a = b + random.randint(0, 100)  # a >= b
        pairs.append((a, b))
        o += a
        c += b

    # 生成 m，使得三种情况都有可能：
    # 1) m >= o
    # 2) m < c
    # 3) c <= m < o
    # 这里随机从一个区间中取值
    # m 范围 [0, max(o + 50, 1)]
    m = random.randint(0, max(o + 50, 1))

    # 以下是原逻辑的实现
    diff = []
    o2 = 0
    c2 = 0
    for a, b in pairs:
        diff.append(a - b)
        o2 += a
        c2 += b

    # 按原代码逻辑判断
    if m >= o2:
        print(0)
    elif m < c2:
        print(-1)
    else:
        diff.sort(reverse=True)
        nd = o2 - m
        for i in range(len(diff)):
            nd -= diff[i]
            if nd <= 0:
                print(i + 1)
                break


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)