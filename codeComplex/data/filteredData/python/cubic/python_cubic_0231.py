from random import randint

mod = 10**9 + 7


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单设定：n, m, l 都与 n 相关，可按需要修改生成策略
    # 保证至少为 1
    n_a = max(1, n)
    n_b = max(1, n)
    n_c = max(1, n)

    # 元素值范围可根据需要调整
    a = [randint(1, 10**3) for _ in range(n_a)]
    b = [randint(1, 10**3) for _ in range(n_b)]
    c = [randint(1, 10**3) for _ in range(n_c)]

    d = {}

    def go(i, j, k):
        val = i * 40401 + j * 201 + k
        if val in d:
            return d[val]

        if i < n_a and j < n_b and k < n_c:
            ret = max(
                a[i] * b[j] + go(i + 1, j + 1, k),
                b[j] * c[k] + go(i, j + 1, k + 1),
                c[k] * a[i] + go(i + 1, j, k + 1),
            )
        elif i < n_a and j < n_b:
            ret = a[i] * b[j] + go(i + 1, j + 1, k)
        elif j < n_b and k < n_c:
            ret = b[j] * c[k] + go(i, j + 1, k + 1)
        elif k < n_c and i < n_a:
            ret = c[k] * a[i] + go(i + 1, j, k + 1)
        else:
            ret = 0

        d[val] = ret
        return ret

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # 返回结果而不是直接打印，调用方可自行处理
    return go(0, 0, 0)


# 示例调用：
# res = main(5)
# print(res)