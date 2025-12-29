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
    # 根据规模 n 生成测试数据
    # 这里假定 n 是原程序中的 n，上限规模
    # s 取与 n 同级别的随机整数
    random.seed(0)
    s = random.randint(0, max(1, n))

    left = 0
    right = 10**30
    while left < right:
        mid = (left + right) // 2
        if bin_func(mid, s) == -1:
            left = mid + 1
        else:
            right = mid
    result = max(0, n - bin_func(left, s) + 1)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，n 可按需要修改或在外部调用 main(n)
    main(10**6)