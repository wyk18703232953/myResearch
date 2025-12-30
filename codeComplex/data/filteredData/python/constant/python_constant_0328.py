import random

def main(n):
    # 生成规模为 n 的测试数据，这里随机生成 0~100 的整数
    b = [random.randint(0, 100) for _ in range(n)]

    ans = 0
    for i in range(n):
        a = b.copy()
        if a[i] == 0:
            continue
        x = a[i]
        a[i] = 0
        full = x // n
        xex = x % n
        for j in range(n):
            a[j] += full
        for j in range(xex):
            a[(i + j + 1) % n] += 1
        pot = 0
        for j in a:
            if j % 2 == 0:
                pot += j
        ans = max(ans, pot)

    print(ans)


if __name__ == "__main__":
    # 示例：用 n = 14 运行一次
    main(14)