import random

def solve(n, m, A):
    # O(31 * (n * m + 2^(2m)))
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
                if ((i | j) == full) and (j in seen):
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


def main(n):
    # 生成规模为 n 的测试数据
    # 这里设置 m 为 5（原程序固定用到 2^m 状态），可根据需要修改
    m = 5

    # 生成随机分数矩阵 A，分数范围可调整
    max_score = 10**9
    A = [[random.randint(0, max_score) for _ in range(m)] for _ in range(n)]

    solve(n, m, A)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)