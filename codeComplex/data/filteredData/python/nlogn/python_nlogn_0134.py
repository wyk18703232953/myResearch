import random

def main(n: int):
    # 生成测试数据
    # x 为长度为 n 的数组，每个元素在 [1, 10] 之间
    x = [random.randint(1, 10) for _ in range(n)]
    # 为保证有意义的规模，令 m 为若干倍的 n，k 初始较小
    m = random.randint(n, 5 * n)
    k = random.randint(0, m)

    x.sort(reverse=True)
    if k >= m:
        print(0)
        return

    for i in range(n):
        k -= 1
        k += x[i]
        if k >= m:
            print(i + 1)
            return

    print(-1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)