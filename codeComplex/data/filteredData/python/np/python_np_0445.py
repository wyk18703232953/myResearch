import random

def solve(x: int, n: int, m: int, a) -> (bool, tuple):
    ans = (-1, -1)
    dp = {}
    for i in range(n):
        temp = 0
        for j in range(m):
            if a[i][j] >= x:
                temp |= (1 << j)
        dp[temp] = i
    full = (1 << m) - 1
    for aa, bb in dp.items():
        for cc, dd in dp.items():
            if aa | cc == full:
                ans = (bb + 1, dd + 1)
                return True, ans
    return False, ans


def main(n: int):
    # 参数化规模：n 为行数，m 自行设定或根据 n 设定
    # 这里简单设定 m 为 5，可按需修改为其他值或函数 f(n)
    m = 5

    # 生成测试数据 a：n 行 m 列，元素在 [0, 10^9] 内
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    l, r = 0, 10**9
    ans = (-1, -1)
    while l <= r:
        mid = (l + r) // 2
        ok, cur_ans = solve(mid, n, m, a)
        if ok:
            ans = cur_ans
            l = mid + 1
        else:
            r = mid - 1

    print(*ans)


if __name__ == "__main__":
    # 示例调用：n = 10
    main(10)