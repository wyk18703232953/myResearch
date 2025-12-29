from math import ceil
import random

def main(n: int):
    # 生成测试数据：
    # k: 组数 [1, n]
    # n: 每人需要的题目数（沿用参数 n，或可自定义范围）
    # s: 每张纸可出题数 [1, max(1, n//2)]
    # p: 每包纸张数 [1, max(1, n)]
    k = random.randint(1, n)
    num_problems = n
    s = random.randint(1, max(1, n // 2))
    p = random.randint(1, max(1, n))

    # 原始逻辑
    sheetsforone = ceil(num_problems / s)
    sheetsfork = sheetsforone * k
    packs = ceil(sheetsfork / p)

    print(int(packs))

if __name__ == "__main__":
    # 示例：调用 main，规模为 100
    main(100)