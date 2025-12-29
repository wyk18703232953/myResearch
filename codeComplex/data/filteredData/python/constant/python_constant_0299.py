from math import ceil
import random

def main(n: int) -> None:
    # 生成测试数据：
    # k: 1~n 的用户数
    # s: 每包可承载的页数 1~n
    # p: 每本书的页数 1~n
    # n: 题意中的 n，直接使用传入的 n 作为题目规模
    k = random.randint(1, max(1, n))
    s = random.randint(1, max(1, n))
    p = random.randint(1, max(1, n))

    n_sheets = ceil(n / s) * k
    n_p = ceil(n_sheets / p)
    print(n_p)

if __name__ == "__main__":
    # 示例：以 n = 100 运行
    main(100)