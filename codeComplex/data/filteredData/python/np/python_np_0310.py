import random

mmm = 998244353

def count_k(ka, k, t):
    if t == 0:  # 00
        return ka[k][0] + ka[k][1] + ka[k][2] + ka[k - 1][3]
    if t == 1:  # 10
        return ka[k - 1][0] + ka[k][1] + ka[k - 2][2] + ka[k - 1][3]
    if t == 2:  # 01
        return ka[k - 1][0] + ka[k - 2][1] + ka[k][2] + ka[k - 1][3]
    if t == 3:  # 11
        return ka[k - 1][0] + ka[k][1] + ka[k][2] + ka[k][3]


def solve(n, k):
    kas = [[0, 0, 0, 0], [1, 0, 0, 1], [0, 1, 1, 0]]

    for _ in range(1, n):
        if len(kas) < k + 1:
            kas.append([0, 0, 0, 0])
            kas.append([0, 0, 0, 0])
        for kk in range(min(len(kas) - 1, k), 1, -1):
            kas[kk] = [count_k(kas, kk, t) % mmm for t in range(4)]

    return (sum(kas[k]) % mmm) if k < len(kas) else 0


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里令 n 为原程序中的 n，
    # 并生成一个与 n 同尺度的 k（1 <= k <= n），可按需要修改生成方式。
    if n < 2:
        n = 2
    k = random.randint(1, n)

    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)