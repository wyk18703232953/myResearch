from math import gcd
from random import randint

def main(n):
    # 1. 生成测试数据
    # 约束：1 <= n <= 15 左右可保证 2^n 暴力可跑
    # 生成难度数组 arr，元素范围设为 [1, 100]
    arr = [randint(1, 100) for _ in range(n)]

    # 生成 l, r, x，保证有意义：
    # l 不大于 r，x 为非负
    total_sum = sum(arr)
    l = randint(0, total_sum // 2) if total_sum > 0 else 0
    r = randint(l, total_sum)      # 保证 l <= r
    x = randint(0, max(arr) - min(arr)) if n > 1 else 0

    # 2. 原逻辑：统计满足条件的非空子集（至少 2 个元素）
    cnt = 0
    for i in range(2, 1 << n):  # 从 2 开始保证至少两位 1（原代码方式）
        b = bin(i)[2:]
        b = '0' * (n - len(b)) + b
        s = 0
        mx = float('-inf')
        mi = float('inf')
        for j in range(n):
            if b[j] == '1':
                mx = max(mx, arr[j])
                mi = min(mi, arr[j])
                s += arr[j]
        if l <= s <= r and mx - mi >= x:
            cnt += 1

    # 3. 输出答案（如需要可改为 return cnt）
    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main(5)，规模 n 可自行调整
    main(5)