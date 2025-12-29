import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设：
    #   k: 参加考试的组数，范围 [1, n]
    #   n: 每组需要的题目数量，使用传入的 n
    #   s: 每页最多题目数量，范围 [1, n]（避免为 0）
    #   p: 每本试卷包含的页数，范围 [1, n]（避免为 0）
    k = random.randint(1, n)
    s = random.randint(1, max(1, n))
    p = random.randint(1, max(1, n))

    sheets = math.ceil(n / s) * k
    result = math.ceil(sheets / p)
    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模
    main(100)