import math

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
    # 将 n 作为 x 的规模，left 采用确定性的函数构造
    # 遍历规模为 n 的输入区间，以保证可规模化
    total = 0
    for i in range(1, n + 1):
        x = i
        left = 1 + (i // 2)
        total ^= solve(x, left)
    # print(total)
    pass
if __name__ == "__main__":
    main(10)