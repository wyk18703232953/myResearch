import random

def main(n):
    # 生成规模为 n 的测试数据 d：每个元素是 [l, r]，且 0 <= l <= r <= 10000
    d = []
    for _ in range(n):
        l = random.randint(0, 10000)
        r = random.randint(l, 10000)
        d.append([l, r])

    s = 0.0

    for k in range(1, 10001):
        p = [min(max((k - l) / (r - l + 1), 1e-20), 1) for l, r in d]

        u = v = 1.0

        for r in p:
            u *= r

        for r in p:
            v *= r
            s += (u - v) * (r - 1) / r

    print(s)

if __name__ == "__main__":
    # 示例：n = 5
    main(5)