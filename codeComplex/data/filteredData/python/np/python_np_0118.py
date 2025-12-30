import random

def main(n):
    # 生成规模为 n 的测试数据：n 个随机非负整数
    # 可根据需要调整随机范围
    xs = [random.getrandbits(60) for _ in range(n)]

    t = [0 for _ in range(2000)]
    c = [0 for _ in range(2000)]

    for i in range(n):
        x = xs[i]
        r = 0
        ok = False
        for j in range(2000):
            if (x >> j) & 1:
                if t[j] != 0:
                    x ^= t[j]
                    r ^= c[j]
                else:
                    t[j] = x
                    c[j] = r ^ (1 << i)
                    ok = True
                    break
        if ok:
            print(0)
            continue
        a = []
        for j in range(2000):
            if (r >> j) & 1:
                a.append(j)
        print(len(a))
        for y in a:
            print(y)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)