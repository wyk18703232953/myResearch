idx1 = 0
idx2 = 0
VALD = 0


def existsequalorbig(mid, m, a):
    global idx1
    global idx2
    global VALD

    abw = []
    hs = set()

    for i in range(len(a)):
        v = 0
        for j in range(m):
            if a[i][j] >= mid:
                v |= 1
            v <<= 1
        v >>= 1
        if v not in hs:
            hs.add(v)
            abw.append([i, v])

    for i in range(len(abw)):
        for j in range(i, len(abw)):
            if abw[i][1] | abw[j][1] == VALD:
                idx1 = abw[i][0]
                idx2 = abw[j][0]
                return True

    return False


def getminmax(n, m, a):
    l = 0
    h = 1000000009

    while l < h:
        mid = (l + h + 1) // 2
        exists = existsequalorbig(mid, m, a)

        if exists:
            l = mid
        else:
            h = mid - 1
    # 原代码未使用 l/h 的结果，这里保持一致
    return l


def generate_test_data(n):
    """
    根据规模 n 生成测试数据:
    - m 固定为 5（可根据需要修改）
    - a 为 n x m 的矩阵，元素为 0..1e9 的整数
    """
    import random

    m = 5
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]
    return m, a


def main(n):
    """
    n 为规模参数：
    - 生成规模为 n 的测试数据
    - 运行原逻辑
    - 返回 (idx1+1, idx2+1)
    """
    global VALD, idx1, idx2

    # 生成测试数据
    m, a = generate_test_data(n)

    # 初始化全局变量
    VALD = (1 << m) - 1
    idx1 = 0
    idx2 = 0

    # 执行原逻辑
    getminmax(n, m, a)

    # 返回 1-based 下标
    return idx1 + 1, idx2 + 1


if __name__ == "__main__":
    # 示例：使用 n=4 运行
    n = 4
    i1, i2 = main(n)
    print(i1, i2)