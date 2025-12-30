from collections import deque
import random

def main(n):
    """
    n: 规模，用于生成测试数据中点的数量 N = n
    边数 M 在这里选择为 n 的 2 倍（可根据需要调整）
    """
    # 生成测试数据
    N = n
    M = max(1, 2 * n)  # 确保至少有一条边
    table = []

    # 随机生成有向边 (s, t, c)
    # 保证 s, t 在 [0, N-1]，权值 c 在 [0, 10^9]
    for _ in range(M):
        s = random.randint(0, N - 1)
        t = random.randint(0, N - 1)
        c = random.randint(0, 10**9)
        table.append((s, t, c))

    def check(k):
        Lin = [0] * N
        edge = [[] for _ in range(N)]
        for s, t, c in table:
            if c > k:
                Lin[t] += 1
                edge[s].append(t)

        Haco = deque()
        ans = []
        for i in range(N):
            if Lin[i] == 0:
                ans.append(i)
                Haco.append(i)

        while Haco:
            x = Haco.pop()
            for y in edge[x]:
                Lin[y] -= 1
                if Lin[y] == 0:
                    ans.append(y)
                    Haco.append(y)
        return ans

    # 二分搜索最小的 ma
    ma = 10 ** 9 + 7
    mi = -1
    while ma - mi > 1:
        mid = (ma + mi) // 2
        if len(check(mid)) == N:
            ma = mid
        else:
            mi = mid

    ans = check(ma)

    # 构建拓扑序的位置映射
    dd = {}
    for pos, node in enumerate(ans):
        dd[node] = pos

    num = 0
    answer = []

    for i in range(M):
        s, t, c = table[i]
        if dd[s] > dd[t] and c <= ma:
            answer.append(i + 1)
            num += 1

    # 输出结果
    print(ma, num)
    if answer:
        print(' '.join(map(str, answer)))
    else:
        print()

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)