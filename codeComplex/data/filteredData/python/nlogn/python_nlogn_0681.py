import random

def main(n):
    # 这里将 n 用作男生数量 b 的规模，女生数量 m 可与 n 相关联
    # 你可以根据需求调整 m 的生成方式
    m = n + 1 if n > 1 else 1  # 示例：m = n + 1，保证有足够女生

    # 生成测试数据
    # 男生数组 b 长度为 n，女生数组 g 长度为 m
    # 值域可以根据需要调整
    b = [random.randint(1, 100) for _ in range(n)]
    g = [random.randint(1, 100) for _ in range(m)]

    # 原逻辑
    b.sort()
    g.sort()

    if b[-1] > g[0]:
        print(-1)
        return

    ans = sum(b) * m
    if g[0] != b[-1]:
        # 需要 n >= 2 才能访问 b[-2]，若 n == 1，则此分支不会被触发，
        # 因为此时 b[-1] == b[-2]，但我们在生成 m 时注意避免极端情况。
        if n >= 2:
            ans += g[0] - b[-2]
    for i in range(1, m):
        ans += g[i] - b[-1]

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 为规模参数
    main(3)