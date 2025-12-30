import random

def main(n):
    # 生成测试数据
    # k 随机在 [0, n * 100] 内
    k = random.randint(0, n * 100)
    a = []
    b = []
    d = []

    # 生成 n 对 (x, y)，保证 x >= y >= 0
    for _ in range(n):
        y = random.randint(0, 100)
        x = y + random.randint(0, 100)
        a.append(x)
        b.append(y)
        d.append(x - y)

    c = 0
    s = sum(a)
    d.sort(reverse=True)

    if sum(b) > k:
        print(-1)
    else:
        while s > k and c < n:
            s -= d[c]
            c += 1
        print(c)

if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要修改 n
    main(5)