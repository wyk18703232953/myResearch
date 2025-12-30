import random

def main(n):
    """
    n 作为规模参数，用来生成 [l, r] 区间：
    这里简单设定：l = 1, r = n + 2
    保证在 n >= 1 时有一定概率存在合法三元组。
    """

    # 根据 n 生成测试数据
    l = 1
    r = n + 2

    # 以下为原始逻辑
    a, b, c = l, l + 1, l + 2

    if l % 2 != 0:
        a, b, c = a + 1, b + 1, c + 1

    if c > r:
        print(-1)
    else:
        print(a, b, c)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)