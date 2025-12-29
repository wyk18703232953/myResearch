from itertools import combinations
import random

def main(n: int):
    # 生成测试数据
    # 假设 mn, mx 范围以及元素范围如下，可按需要调整
    # 生成一个升序区间 [mn, mx]，并生成 n 个元素
    # 保证 mn <= mx
    # 为了能产生一定数量合法子集，设定元素范围在 [1, 100]
    arr = [random.randint(1, 100) for _ in range(n)]
    
    # 设定 mn, mx, diff
    # 使用 arr 的性质构造合理区间
    total_sum = sum(arr)
    mn = total_sum // (2 * n if n > 0 else 1)  # 一个较小的下界
    mx = total_sum // 2 if total_sum // 2 >= mn else mn  # 上界不少于下界
    diff = max(1, (max(arr) - min(arr)) // 4 if n > 1 else 1)

    # 核心逻辑：统计符合条件的子集数量
    ans = sum(
        1
        for i in range(2, n + 1)
        for x in combinations(arr, i)
        if mn <= sum(x) <= mx and max(x) - min(x) >= diff
    )

    print(ans)


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(5)