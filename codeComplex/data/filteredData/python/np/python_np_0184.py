import random

def main(n):
    # 生成测试数据
    # 约束：1 <= l <= r，x >= 0，难度数组为正整数
    # 随机生成难度值
    arr = [random.randint(1, 10**6) for _ in range(n)]

    # 生成 l, r（总难度区间）
    total_sum = sum(arr)
    if total_sum == 0:
        l, r = 0, 0
    else:
        l = random.randint(0, total_sum)
        r = random.randint(l, total_sum)

    # 生成 x（最大最小差值下限）
    max_diff = max(arr) - min(arr)
    x = random.randint(0, max_diff if max_diff > 0 else 0)

    # 原逻辑
    res = 0
    for j in range(1, 1 << n):
        chosen = [arr[i] for i in range(n) if (j >> i) & 1]
        s = sum(chosen)
        if max(chosen) - min(chosen) >= x and l <= s <= r:
            res += 1

    print(res)

if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要调整
    main(5)