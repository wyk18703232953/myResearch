import random

def main(n):
    # 生成测试数据：k 在合法范围 0..(2*(n-2)) 内随机取值
    # 因为这段构造逻辑最多能放 2*(n-2) 个 '#'
    if n < 3:
        # 原逻辑要求 n 至少为 3（否则中点和左右两端逻辑都不合理）
        # 对于过小的 n，直接返回一个简单示例
        k = 0
    else:
        max_k = 2 * (n - 2)
        k = random.randint(0, max_k)

    out = [['.'] * n for _ in range(4)]

    if k & 1:
        out[1][n >> 1] = '#'
        k -= 1

    for i in range(1, 3):
        l, r = 1, n - 2
        for j in range(1, n - 2):
            if k:
                k -= 1
                if j & 1:
                    out[i][l] = '#'
                    l += 1
                else:
                    out[i][r] = '#'
                    r -= 1

    for i in range(1, 3):
        if k:
            k -= 1
            out[i][n >> 1] = '#'

    print('YES')
    for row in out:
        print(''.join(row))


if __name__ == "__main__":
    # 示例调用：可以修改 n 来测试不同规模
    main(7)