import random

def main(n):
    # 生成测试数据：
    # 随机生成 k，范围 [1, 2^(n+1)]，保证有一定覆盖度
    if n <= 0:
        return
    k = random.randint(1, 2 ** (min(n + 1, 30)))  # 防止爆掉

    # 原逻辑开始
    if n == 2 and k == 3:
        print("NO")
        return

    if n >= 32:
        print("YES", n - 1)
        return

    val = [0]
    for i in range(1, n + 1):
        val.append(4 * val[i - 1] + 1)

    if val[n] < k:
        print("NO")
        return

    s = 0
    t = 2
    while s + t - 1 <= k and n > 0:
        s = s + t - 1
        t *= 2
        n -= 1

    print("YES", n)


if __name__ == "__main__":
    # 示例：调用 main，规模可修改
    main(10)