import math
import random

def gaosi(x):
    if x == 1:
        return 1
    else:
        return ((1 + x) * x) / 2

def calc(mid, total, left):
    return gaosi(mid) - (total - mid) - left

def solve(x, left):
    if x == 1 and left == 1:
        return 0
    l = 1
    r = x
    while True:
        mid = (l + r) // 2
        result = calc(mid, x, left)
        if result == 0:
            return x - mid
        elif result > 0:
            r = mid
        elif result < left:
            l = mid

def main(n):
    # 根据规模 n 生成测试数据
    # 约定：x = n，left 在 [1, x] 随机生成
    x = max(1, n)
    left = random.randint(1, x)
    ans = solve(x, left)
    print(f"x={x}, left={left}, answer={ans}")

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)