import random

def main(n):
    # 生成测试数据：4 个 n×n 的 0/1 矩阵（用字符串表示每行）
    # 每次调用 f 时消费一整个矩阵的数据
    def gen_matrix():
        return ["".join(random.choice("01") for _ in range(n)) for _ in range(n)]

    matrices = [gen_matrix() for _ in range(4)]
    skip_matrices = [gen_matrix() for _ in range(4)]  # 用来模拟原代码里被丢弃的 rd()

    # 将原来的 rd() 替换为从给定矩阵迭代读行
    def f(n, t, mat, skip_mat=None):
        # mat: 当前实际使用的矩阵（列表，每个元素是长度为 n 的 "01" 字符串）
        # skip_mat: 如提供，则模拟原代码里多读一次但不使用
        rows_iter = iter(mat)

        def rd():
            # 原代码里 input() 读一行，map(int, input()) 按字符转 int
            # 这里从矩阵中取一行字符串
            line = next(rows_iter)
            return map(int, line)

        a = sum((i + j) & 1 == x  # 注意括号以保持原逻辑： (i + j) & 1
                for i in range(n)
                for j, x in enumerate(rd()))
        if t < 3 and skip_mat is not None:
            # 模拟原来的 “额外读一次但丢弃”
            _ = skip_mat  # 这里不再真正消费，因为我们只是生成测试数据
        return a

    # 计算四次 f，对应原代码：[f(n, i) for i in range(4)]
    m = sorted(f(n, i, matrices[i], skip_matrices[i]) for i in range(4))
    result = 2 * n * n + m[0] + m[1] - m[2] - m[3]
    print(result)

# 示例：直接运行时给一个默认规模
if __name__ == "__main__":
    main(5)