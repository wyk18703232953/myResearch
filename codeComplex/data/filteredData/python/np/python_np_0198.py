from itertools import combinations
import random

def check(j, l, r, x):
    s = sum(j)
    if l <= s <= r and (max(j) - min(j)) >= x:
        return 1
    return 0

def main(n):
    # 生成测试数据
    # c: n 个正整数，范围可根据需要调整
    c = [random.randint(1, 1000) for _ in range(n)]
    # 约束参数，可根据生成数据的规模自适应设置
    total_sum = sum(c)
    l = total_sum // 4          # 下界
    r = (total_sum * 3) // 4    # 上界
    x = max(1, (max(c) - min(c)) // 4)  # 难度差下限

    count = 0
    for i in range(2, n + 1):
        for j in combinations(c, i):
            if check(j, l, r, x):
                count += 1

    print(count)

if __name__ == "__main__":
    # 示例：调用 main，规模可按需修改
    main(5)