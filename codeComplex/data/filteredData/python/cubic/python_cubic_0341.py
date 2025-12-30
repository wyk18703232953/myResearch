import random

M = 998244353


def main(n: int) -> int:
    # 生成规模为 n 的测试数据：这里生成 1..10^9 范围内的随机整数
    # 可根据需要调整数据分布
    l = [random.randint(1, 10**9) for _ in range(n)]

    # 原始逻辑开始
    l = sorted(l)[::-1]
    out = [0] * n
    big = 0
    if n >= 2 and l[0] >= 2 * l[1]:
        out[1] = 1
        big = 1

    for i in range(2, n):
        new = [0] * n
        bigN = 0
        for j in range(i):
            if l[j] >= 2 * l[i]:
                big += out[j]
            else:
                new[j] += out[j] * (i - 1)
                new[j] %= M

        new[i] = big
        bigN = (i * big) % M

        out = new
        big = bigN

    return (big + sum(out)) % M


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    result = main(5)
    print(result)