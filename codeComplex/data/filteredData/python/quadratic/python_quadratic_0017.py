from math import sqrt

def main(n):
    # n 表示 a 的规模，同时生成 a 个 x 坐标
    a = max(1, n)
    r = max(1, n // 2 + 1)
    x = [i % (2 * r + 1) for i in range(a)]
    y = [0] * a
    outputs = []
    for i in range(a):
        h = r
        for j in range(i):
            if abs(x[i] - x[j]) <= 2 * r:
                h = max(h, sqrt((2 * r) ** 2 - (x[i] - x[j]) ** 2) + y[j])
        y[i] = h
        outputs.append(h)
    print(" ".join(str(v) for v in outputs))


if __name__ == "__main__":
    main(10)