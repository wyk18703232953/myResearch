import random

def main(n: int):
    # 1. 根据规模 n 生成测试数据
    #   a: 数组长度
    #   z: 长度为 a 的整数数组
    #
    # 这里令 a = n，并生成 [-10n, 10n] 区间内的随机整数
    a = n
    if a <= 0:
        return

    z = [random.randint(-10 * n, 10 * n) for _ in range(a)]

    # 2. 保留原始逻辑
    ans = []
    k = len(z)
    for i in range(len(z)):
        if (z[i] - i) % len(z) == 0:
            ans.append((z[i] - i) // k)
        else:
            ans.append((z[i] - i) // k)
            ans[-1] += 1
    t = min(ans)
    print(ans.index(t) + 1)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)