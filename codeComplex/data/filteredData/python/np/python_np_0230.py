from itertools import combinations
from random import randint

mod = 1000000007

def main(n: int):
    # 生成测试数据
    # 题意：给定 n, l, r, x 和数组 arr，统计满足条件的子集个数
    # 这里根据 n 随机生成一组数据：
    #   arr: n 个 1~1000 的随机数
    #   l, r: 根据 arr 的整体范围生成一个合理区间
    #   x: 难度差阈值，取一个相对较小的随机值
    arr = [randint(1, 1000) for _ in range(n)]
    total_sum = sum(arr)
    min_val = min(arr)
    max_val = max(arr)

    # 生成一个合理的 [l, r] 区间
    # 保证 l <= r 且区间落在 [0, total_sum] 内
    # 这里简单取：
    #   l 为总和的 1/4 左右
    #   r 为总和的 3/4 左右
    if total_sum == 0:
        l, r = 0, 0
    else:
        l = total_sum // 4
        r = (3 * total_sum) // 4
        if l > r:
            l, r = r, l

    # x 为元素范围的 1/3 左右（至少为 1）
    if max_val == min_val:
        x = 1
    else:
        x = max(1, (max_val - min_val) // 3)

    # 原逻辑
    count = 0
    for i in range(2, n + 1):
        for comb in combinations(arr, i):
            s = sum(comb)
            if l <= s <= r and max(comb) - min(comb) >= x:
                count += 1

    # 输出结果（同时可输出生成的测试数据，方便调试）
    print("n =", n)
    print("arr =", arr)
    print("l =", l, "r =", r, "x =", x)
    print("answer =", count)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)