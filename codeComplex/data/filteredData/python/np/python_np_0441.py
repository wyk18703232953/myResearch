import random

def main(n: int):
    # 随机生成 m（列数），范围可按需调整
    m = random.randint(1, min(10, max(1, n)))  # 示例：m 在 [1, min(10, n)] 内

    # 生成测试数据矩阵 a，元素范围 [0, 10^9]
    MAX_VAL = 10 ** 9
    a = [[random.randint(0, MAX_VAL) for _ in range(m)] for _ in range(n)]

    ans = []
    lo = 0
    hi = MAX_VAL

    def vanguda(mid: int) -> bool:
        nonlocal ans
        f = {}
        for i in range(n):
            bi = 0
            for j in range(m):
                if a[i][j] >= mid:
                    bi += 1
                bi <<= 1
            f[bi >> 1] = i
        full_mask = (1 << m) - 1
        for aa, bb in f.items():
            for cc, dd in f.items():
                if aa | cc == full_mask:
                    ans = (bb + 1, dd + 1)
                    return True
        return False

    while lo <= hi:
        mid = (lo + hi) // 2
        if vanguda(mid):
            lo = mid + 1
        else:
            hi = mid - 1

    # 输出结果
    if ans:
        print(*ans)
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行指定
    main(5)