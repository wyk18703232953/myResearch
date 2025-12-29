import random

def main(n: int):
    # 生成长度为 n 的数组，元素为 1..n 的随机排列（便于测试）
    l = list(range(1, n + 1))
    random.shuffle(l)

    # 生成查询次数 m（这里设为 n，当然可按需要调整规则）
    m = n

    odd = 0
    # 初始逆序对奇偶性计算
    for i in range(n):
        for j in range(i, n):
            if l[i] > l[j]:
                odd ^= 1

    ans = []
    # 生成 m 个随机查询区间 [ll, r]，1-based 且 ll <= r
    for _ in range(m):
        ll = random.randint(1, n)
        r = random.randint(ll, n)
        k = r - ll + 1
        if (k * (k - 1) // 2) % 2:
            odd ^= 1
        ans.append("odd" if odd else "even")

    print('\n'.join(ans))


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时根据需要修改 n
    main(5)