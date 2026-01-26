import math

def gaosi(x):
    if x == 1:
        return 1
    else:
        return ((1 + x) * x) / 2

def calc(mid, total, left):
    return gaosi(mid) - (total - mid) - left

def experiment(x, left):
    if x == 1 and left == 1:
        return 0

    l = 1
    r = x
    # 为了保证可终止，这里加入有限步数约束
    # 同时根据原逻辑进行二分调整
    for _ in range(1000):
        mid = (l + r) // 2
        result = calc(mid, x, left)
        if result == 0:
            return x - mid
        elif result > 0:
            r = mid
        elif result < left:
            l = mid
        # 为防止死循环，区间不再缩小时退出
        if r - l <= 1:
            break
    return -1

def main(n):
    # 将 n 映射为输入规模：x = n, left = n // 2
    x = max(1, n)
    left = max(1, n // 2)
    result = experiment(x, left)
    print(result)

if __name__ == "__main__":
    main(10)