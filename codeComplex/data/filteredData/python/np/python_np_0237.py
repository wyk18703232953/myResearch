from itertools import combinations
import random

def main(n):
    # 生成测试数据
    # 为了可控，设定：题目难度在 [1, 1000] 内
    # l, r, x 也从数据范围中合理生成
    random.seed(0)  # 如需每次不同，可去掉这一行

    c = [random.randint(1, 1000) for _ in range(n)]
    total_sum = sum(c)
    min_c, max_c = min(c), max(c)

    # 生成 l, r, x，保证有一定概率存在可行解
    l = random.randint(1, max(1, total_sum // 2))
    r = random.randint(l, total_sum)
    x = random.randint(0, max_c - min_c if max_c > min_c else 0)

    ways_to_choose = 0
    for length in range(2, n + 1):
        for p in combinations(c, length):
            problemset = sorted(p)
            s = sum(problemset)
            if l <= s <= r and problemset[-1] - problemset[0] >= x:
                ways_to_choose += 1

    print(ways_to_choose)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)