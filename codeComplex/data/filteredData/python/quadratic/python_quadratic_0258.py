def main(n):
    # 映射关系：
    # - 原程序中：n, a, b = map(int, input().split())
    # - 这里：把输入规模参数 n 映射为原来的 "矩阵规模 n"
    # - 为了让 a, b 随规模变化但仍保持确定性，构造 a, b 为 n 的简单函数
    #
    # 保证与原逻辑兼容的一种方式：
    # - 令 a = 1
    # - 令 b = 1
    # 这样对于所有 n >= 1，原程序都是合法的输入，并且逻辑统一、可扩展、易于做复杂度实验
    #
    # 若需要更丰富的结构，可以改为如：
    #   a = 1
    #   b = 1 + (n % 2)
    # 但那会触发 min(a, b) > 1 的 NO 分支，不利于观察矩阵构造过程的复杂度。
    #
    # 因此这里选择固定 a = b = 1，仅将矩阵规模与实验规模 n 绑定。
    a = 1
    b = 1

    if min(a, b) > 1 or ((n, a, b) in ((2, 1, 1), (3, 1, 1))):
        # print("NO")
        pass
        return

    res = [[0] * n for _ in range(n)]
    for i in range(0, n - max(a, b)):
        res[i][i + 1] = res[i + 1][i] = 1
    if a == 1:
        res = [[e ^ 1 for e in l] for l in res]

    # print("YES")
    pass
    for i in range(n):
        res[i][i] = 0
        # print(*res[i], sep='')
        pass
if __name__ == "__main__":
    # 示例：以 n = 5 作为输入规模运行一次
    main(5)