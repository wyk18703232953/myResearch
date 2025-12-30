import random

def bs(c, t):
    l, r = 0, t - 1
    while l <= r:
        mid = (l + r) >> 1
        if ((2 * t - mid - 1) * mid) // 2 + 1 < c:
            l = mid + 1
        else:
            r = mid - 1
    return r + 1

def main(n):
    # 规模 n 用来生成测试数据
    # 假设 tubos = n，casas 在 [1, 最大可覆盖值] 内随机生成
    tubos = n
    # 最大可覆盖的 casas 数
    max_casas = ((2 * tubos - 0 - 1) * 0) // 2 + 1  # 其实对 mid=0 是 1
    # 为了使搜索有意义，考虑 mid=tubos 时的上界
    max_casas = ((2 * tubos - tubos - 1) * tubos) // 2 + 1  # mid=tubos-1 的最大值+安全余量
    casas = random.randint(1, max_casas)

    res = bs(casas, tubos)
    print(-1 if res == tubos else res)

if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)