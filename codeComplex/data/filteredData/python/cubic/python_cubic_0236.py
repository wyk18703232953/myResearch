import random

def main(n):
    # 1. 生成规模 R, G, B（这里都设为 n，可按需要修改生成规则）
    R = G = B = n

    # 2. 生成测试数据：长度分别为 R, G, B 的随机正整数数组
    # 数值范围可按需要调整，这里用 1~100
    r = [random.randint(1, 100) for _ in range(R)]
    g = [random.randint(1, 100) for _ in range(G)]
    b = [random.randint(1, 100) for _ in range(B)]

    # 原逻辑开始
    def f(t):
        i, j, k = t
        return (i + 1) * (G + 1) * (B + 1) + (j + 1) * (B + 1) + (k + 1)

    max_area = [None] * ((R + 1) * (G + 1) * (B + 1) + 1)

    def get_max_area(i, j, k):
        temp = f((i, j, k))
        if max_area[temp] is not None:
            return max_area[temp]

        x1 = x2 = x3 = 0
        if i >= 0 and j >= 0:
            x1 = get_max_area(i - 1, j - 1, k) + r[i] * g[j]
        if i >= 0 and k >= 0:
            x2 = get_max_area(i - 1, j, k - 1) + r[i] * b[k]
        if j >= 0 and k >= 0:
            x3 = get_max_area(i, j - 1, k - 1) + g[j] * b[k]

        max_area[temp] = max(x1, x2, x3)
        return max_area[temp]

    r.sort()
    g.sort()
    b.sort()

    ans = get_max_area(R - 1, G - 1, B - 1)
    print(ans)
    return ans

# 示例调用
# main(3)