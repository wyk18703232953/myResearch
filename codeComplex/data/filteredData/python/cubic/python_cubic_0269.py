import random

def f(r, g, b, n, m, k, mat):
    if (n >= 1 and m >= 1) or (k >= 1 and m >= 1) or (n >= 1 and k >= 1):
        if mat[n][m][k] != -1:
            return mat[n][m][k]
        a1 = b1 = c1 = 0
        if n >= 1 and m >= 1:
            a1 = r[n - 1] * g[m - 1] + f(r, g, b, n - 1, m - 1, k, mat)
        if k >= 1 and m >= 1:
            b1 = b[k - 1] * g[m - 1] + f(r, g, b, n, m - 1, k - 1, mat)
        if n >= 1 and k >= 1:
            c1 = r[n - 1] * b[k - 1] + f(r, g, b, n - 1, m, k - 1, mat)
        mat[n][m][k] = max(a1, b1, c1)
        return mat[n][m][k]
    return 0


def main(n):
    """
    n: 规模参数，用于生成三种颜色数组的长度。
       这里为了简化，令三个数组长度都为 n。
    """
    # 生成测试数据：三个长度为 n 的数组，元素为 1..100 的随机整数
    len_r = len_g = len_b = n
    r = [random.randint(1, 100) for _ in range(len_r)]
    g = [random.randint(1, 100) for _ in range(len_g)]
    b = [random.randint(1, 100) for _ in range(len_b)]

    # 排序与原程序一致
    r.sort()
    g.sort()
    b.sort()

    # DP 数组
    mat = [[[-1 for _ in range(len_b + 1)]
            for _ in range(len_g + 1)]
           for _ in range(len_r + 1)]

    ans = f(r, g, b, len_r, len_g, len_b, mat)
    print(ans)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)