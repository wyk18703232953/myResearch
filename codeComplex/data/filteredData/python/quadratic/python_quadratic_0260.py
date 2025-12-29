import random

def main(n: int):
    # 生成满足原逻辑前置条件的 a, b
    # 条件从原代码推断：
    # 1) a <= n, b <= n
    # 2) 若 a == 1 且 b == 1，则 n 不能为 2 或 3
    # 3) 若 n == 1，则必须 a == 1 且 b == 1
    # 4) min(a, b) == 1
    # 总结：min(a, b) == 1，a <= n，b <= n，且 (a, b, n) 不落入被判 NO 的情况

    if n == 1:
        a, b = 1, 1
    elif n in (2, 3):
        # a==1 and b==1 会被判 NO，所以随机选一个 >1 的，另一个为 1，且 <= n
        if n == 2:
            a, b = 1, 2
        else:  # n == 3
            a, b = 1, 2
    else:
        # n >= 4
        # 确保 min(a, b) == 1，且不同时为 1（否则在 n==2 or 3 会 NO，这里 n>=4 则允许）
        # 这里随机生成，满足条件即可
        if random.choice([True, False]):
            a = 1
            b = random.randint(1, n)
            if b == 1:
                b = random.randint(2, n)
        else:
            b = 1
            a = random.randint(1, n)
            if a == 1:
                a = random.randint(2, n)

    # 主逻辑开始（移除 input，使用上面生成的 n, a, b）
    if a > n:
        print('NO')
        return
    if b > n:
        print('NO')
        return
    if a == 1 and b == 1:
        if n == 2 or n == 3:
            print('NO')
            return
    if (n == 1 and a > 1) or (n == 1 and b > 1):
        print('NO')
        return
    if min(a, b) > 1:
        print('NO')
        return

    def check(mat):
        # BFS 统计连通块数量（原代码逻辑，略有缩进错误，保持结构但修正为可用版本）
        vis = [0] * n
        cnt = 0
        for i in range(n):
            if vis[i] == 0:
                q = [i]
                cnt += 1
                vis[i] = 1
                while q:
                    t = q.pop(0)
                    for j in range(n):
                        if mat[t][j] == 1 and vis[j] == 0:
                            vis[j] = 1
                            q.append(j)
        return cnt

    mat = [[0 for _ in range(n)] for _ in range(n)]
    m = max(a, b)
    j = 1
    for i in range(n):
        if j < n:
            mat[i][j] = 1
            mat[j][i] = 1
        j += 1
    for i in range(m - 1):
        curr = n - i - 1
        for j in range(n):
            if mat[curr][j] == 1:
                mat[curr][j] = 0
                mat[j][curr] = 0

    if b == 1:
        print('YES')
        for i in range(n):
            print(*mat[i], sep='')
    else:
        print('YES')
        for i in range(n):
            for j in range(n):
                mat[i][j] = 1 - mat[i][j]
        for i in range(n):
            mat[i][i] = 0
        for i in range(n):
            print(*mat[i], sep='')


# 示例调用（可按需要注释/修改）
if __name__ == "__main__":
    main(5)