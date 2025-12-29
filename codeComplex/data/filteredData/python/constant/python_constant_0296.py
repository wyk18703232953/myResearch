import random
import math

def main(n: int):
    # 随机生成测试数据：
    # k: 朋友数量（1 ~ n）
    # n: 每人需要的页数（1 ~ n）
    # s: 每张纸能裁出的页数（1 ~ n）
    # p: 每包纸的张数（1 ~ n）
    k = random.randint(1, n)
    need_pages = random.randint(1, n)
    s = random.randint(1, n)
    p = random.randint(1, n)

    # 计算需要的纸张数
    sheets = (need_pages + s - 1) // s
    # 计算需要的包数
    result = (sheets * k + p - 1) // p

    print(result)


if __name__ == "__main__":
    # 示例：规模为 100
    main(100)