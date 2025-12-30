import random

def solve(n, m, A):
    # O(31*( 5*n + 2^m * 2^m )) but original comment assumes m<=5
    ans = ()
    nstats = 2 ** m

    def judge(finalScore):
        nonlocal ans
        seen = {}
        for i, scores in enumerate(A):
            sta = 0
            for e in scores:
                sta = sta * 2 + (e >= finalScore)
            seen[sta] = i

        full = nstats - 1
        for i in range(nstats):
            if i not in seen:
                continue
            for j in range(nstats):
                if ((i | j) == full) and j in seen:
                    ans = (seen[i], seen[j])
                    return True
        return False

    l = 0
    r = 2 ** 31 - 1
    while l < r:
        mid = l + (r - l) // 2
        if not judge(mid):
            r = mid
        else:
            l = mid + 1

    print(ans[0] + 1, ans[1] + 1)


def main(n: int):
    # 生成规模为 n 的测试数据
    # 限制 m 较小以保证原算法可运行，保持与原题意接近（m<=5）
    m = min(5, max(1, n if n <= 5 else 5))

    # 生成 A：n 行，每行 m 个分数，范围 0..1e9
    A = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    solve(n, m, A)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)