import random


def main(n: int):
    # 自动生成测试数据：n 行，m 列
    # 为了可控，这里设定 m = min(10, n)；你也可以按需修改为固定值
    m = min(10, n if n > 0 else 1)

    # 生成 a：n x m 的整数矩阵，元素范围 [0, 1e9]
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    ans = []

    def check(mid: int) -> bool:
        nonlocal ans
        dic = {}
        for i in range(n):
            bit = 0
            for j in range(m):
                if a[i][j] >= mid:
                    bit += 1
                bit <<= 1
            dic[bit >> 1] = i
        full = (1 << m) - 1
        for x, idx in dic.items():
            for y, idy in dic.items():
                if x | y == full:
                    ans = [idx + 1, idy + 1]
                    return True
        return False

    le = 0
    ri = 10**9
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri = mid - 1

    # 输出结果
    if ans:
        print(ans[0], ans[1])
    else:
        # 理论上不会发生（总能选两行覆盖所有列），但为稳妥处理
        print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(5)