import random

def main(n: int):
    """
    n 为规模参数，用于生成测试数据：
    - 令 N = max(1, n // 2)
    - 令 M = max(1, n)
    - b 为长度 N 的整数数组
    - g 为长度 M 的整数数组
    """
    # 生成测试数据
    N = max(1, n // 2)
    M = max(1, n)

    # 随机生成正整数，范围可按需调整
    b = [random.randint(1, 100) for _ in range(N)]
    g = [random.randint(1, 100) for _ in range(M)]

    # 以下为原程序逻辑
    if max(b) > min(g):
        ans = -1
    elif max(b) == min(g):
        ans = M * sum(b)
        maxi = max(b)
        for i in range(M):
            if maxi == g[i]:
                continue
            else:
                ans += g[i] - maxi
    else:
        ans = M * sum(b)
        b.sort(reverse=True)
        for i in range(M):
            if i == 0:
                ans += g[i] - b[1]
            else:
                ans += g[i] - b[0]

    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)