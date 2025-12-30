import random

def main(n):
    # 生成一个 n x n 的随机网格，元素为 '.' 或 '#'
    m = n
    b = []
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.choice(['.', '#']))
        b.append(row)
        a.append([0 for _ in range(m)])

    def check(e, r, q):
        # 判断能否在 (e, r) 为左上角放置一个 3x3 的 '#' 边框
        if e >= 0 and r >= 0 and e + 2 < n and r + 2 < m:
            if (
                b[e][r] == '#' and b[e + 1][r] == '#' and b[e + 2][r] == '#' and
                b[e + 2][r + 1] == '#' and b[e + 2][r + 2] == '#' and
                b[e + 1][r + 2] == '#' and b[e][r + 2] == '#' and b[e][r + 1] == '#'
            ):
                # 标记这些位置被覆盖（原代码此处用的是 '=='，看起来是 bug，这里改成赋值）
                a[e][r] = 1
                a[e + 1][r] = 1
                a[e + 2][r] = 1
                a[e + 2][r + 1] = 1
                a[e + 2][r + 2] = 1
                a[e + 1][r + 2] = 1
                a[e][r + 2] = 1
                a[e][r + 1] = 1
                return True
        if q == 1:
            return False
        # 递归向周围位置尝试
        return (
            check(e, r - 1, 1) or check(e, r - 2, 1) or
            check(e - 1, r - 2, 1) or check(e - 2, r - 2, 1) or
            check(e - 2, r - 1, 1) or check(e - 2, r, 1) or
            check(e - 1, r, 1)
        )

    # 核心检查逻辑
    for i in range(n):
        for j in range(m):
            if b[i][j] == '#':
                if (not check(i, j, 0)) and a[i][j] == 0:
                    print("NO")
                    return

    print("YES")


# 示例：直接执行文件时跑一组规模为 5 的测试
if __name__ == "__main__":
    main(5)