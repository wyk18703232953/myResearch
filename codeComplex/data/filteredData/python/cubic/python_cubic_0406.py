import random

def main(n):
    # 生成测试数据
    # n: 行数
    # 我们让 m = n（也可以按需修改为其他函数），k = 2 * n（保证为偶数）
    m = n
    k = 2 * n

    # 生成 a: n 行 m-1 列（如果 m == 1，则为空）
    a = []
    for i in range(n):
        row = []
        for j in range(max(0, m - 1)):
            row.append(random.randint(1, 10))
        a.append(row)

    # 生成 b: n-1 行 m 列（如果 n == 1，则为空）
    b = []
    for i in range(max(0, n - 1)):
        row = []
        for j in range(m):
            row.append(random.randint(1, 10))
        b.append(row)

    # 以下是原 solve() 逻辑改造，无 input()
    if k % 2:
        ans = [-1] * m
        for _ in range(n):
            print(*ans)
        return

    k //= 2
    pre = [[0] * m for _ in range(n)]
    cur = [[10**9] * m for _ in range(n)]

    for _ in range(k):
        cur = [[10**9] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i:
                    cur[i][j] = min(cur[i][j], pre[i - 1][j] + b[i - 1][j])
                if i < n - 1:
                    cur[i][j] = min(cur[i][j], pre[i + 1][j] + b[i][j])
                if j:
                    cur[i][j] = min(cur[i][j], pre[i][j - 1] + a[i][j - 1])
                if j < m - 1:
                    cur[i][j] = min(cur[i][j], pre[i][j + 1] + a[i][j])
        pre = cur

    for i in range(n):
        cur[i] = [cur[i][j] * 2 for j in range(m)]
        print(*cur[i])


# 示例调用：
# main(3)