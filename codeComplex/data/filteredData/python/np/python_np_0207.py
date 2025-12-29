from itertools import combinations
import random

def main(n):
    # 1. 生成测试参数 least, highest, x
    # 随机生成 n 个元素的列表，取值范围 1~100
    l = [random.randint(1, 100) for _ in range(n)]
    
    # 为了保证 least 和 highest 有意义，我们根据数组和来设置区间
    sum_l = sum(l)
    least = random.randint(0, sum_l)               # 最小总和下限
    highest = random.randint(least, sum_l)         # 最大总和上限，保证 >= least

    # x 为元素差值要求
    x = random.randint(0, 100)

    cnt = 0
    for i in range(2, n + 1):
        combination = [list(c) for c in combinations(l, i)]
        for comb in combination:
            comb.sort()
            total = sum(comb)
            if least <= total <= highest and comb[-1] - comb[0] >= x:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(5)