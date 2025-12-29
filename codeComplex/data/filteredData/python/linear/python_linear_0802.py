import random

def main(n):
    # 生成测试数据
    # n: 测试规模，这里用作 m 的大小，同时设置 k 和 pi 的范围
    m = n
    if m <= 0:
        print(0)
        return

    # 随机生成 k，避免为 0
    k = random.randint(1, max(1, n))

    # 生成一个递增的 pi 序列，元素值在 [1, 2*n] 范围内
    pi = sorted(random.sample(range(1, 2 * n + 1), m))

    # 原逻辑开始
    num = 1
    ans = 0
    i = 0
    while i < m:
        temp = (pi[i] - num) // k
        temp2 = i
        i += 1
        while i < m:
            if temp != (pi[i] - num) // k:
                break
            i += 1
        num += (i - temp2)
        ans += 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(10)