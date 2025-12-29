from math import ceil
import random

def main(n):
    # 生成测试数据：
    # 当 n 为规模参数，这里简单令：
    #   k = n      （用户数）
    #   n_pages = n（每个用户需要的页数）
    #   s = max(1, n // 3)（每包纸张的页数）
    #   p = max(1, n // 2)（每本笔记本的页数）
    #
    # 可以根据需要自定义生成规则；这里保持确定性和简单性。
    k = n
    n_pages = n
    s = max(1, n // 3)
    p = max(1, n // 2)

    # 原始逻辑
    spp = ceil(n_pages / s)  # 每个用户需要的纸包数
    tots = spp * k           # 所有用户需要的纸包总数
    result = ceil(tots / p)  # 需要的笔记本数量

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)