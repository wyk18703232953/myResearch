import random


def main(n: int):
    # 1. 生成测试数据
    # 随机生成 m，保证 1 <= m <= n（也可自行调整规则）
    m = max(1, n // 2)
    # 随机生成矩阵 a，元素范围 [0, 1e9]
    MAXV = 10**9
    a = [[random.randint(0, MAXV) for _ in range(m)] for _ in range(n)]

    ans = []
    le = 0
    ri = int(1e9)

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
                    ans = (idx + 1, idy + 1)
                    return True
        return False

    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri -= 1

    # 输出两行：第一行为 n 和 m，第二行起为矩阵内容，然后是答案
    print(n, m)
    for row in a:
        print(" ".join(map(str, row)))
    print(ans[0], ans[1])


if __name__ == "__main__":
    # 示例规模，可在外部调用 main(n) 进行测试
    main(5)