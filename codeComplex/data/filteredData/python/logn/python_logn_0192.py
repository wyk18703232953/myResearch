import random

def bin_func(num, s):
    i = 9 * num * 11
    for _ in range(100):
        add = 0
        a = str(i)
        for k in range(10):
            add += a.count(str(k)) * k
        if i - add >= s:
            return i
        i += 1
    return -1

def main(n):
    # 根据 n 生成测试数据：这里令 s = n 的一个函数，例如 s = n // 2
    s = n // 2

    left = 0
    right = 10**30
    while left < right:
        mid = (left + right) // 2
        if bin_func(mid, s) == -1:
            left = mid + 1
        else:
            right = mid
    ans = max(0, n - bin_func(left, s) + 1)
    print(ans)

if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(1000)