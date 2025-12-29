from itertools import combinations
import random

def main(n: int):
    # 生成测试数据
    # 约束条件可根据需要调整，这里给出一个合理由于演示的生成方案
    # 生成 n 个题目难度值
    arr = [random.randint(1, 100) for _ in range(n)]
    # 生成 l, r, x
    # 确保 l <= r，x 为难度差阈值
    min_sum_possible = min(arr) * 2
    max_sum_possible = sum(sorted(arr, reverse=True)[:n])  # 最大可能和（其实就是总和）
    l = random.randint(min_sum_possible, max_sum_possible // 2 if max_sum_possible // 2 >= min_sum_possible else max_sum_possible)
    r = random.randint(l, max_sum_possible)
    x = random.randint(0, max(arr) - min(arr) if n > 1 else 0)

    ans = 0
    for i in range(2, n + 1):
        brr = combinations(arr, i)
        for j in brr:
            s = sum(j)
            if l <= s <= r and max(j) - min(j) >= x:
                ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(5)