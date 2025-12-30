import random

def main(n):
    # 生成测试数据：m 在 1 到 2^(n-1) 之间
    if n <= 0:
        return
    max_m = 1 << (n - 1)
    m = random.randint(1, max_m)

    a = [0] * (n + 1)
    l, r = 1, n

    for i in range(1, n + 1):
        if m <= 1 << max((n - i - 1), 0):
            a[l] = i
            l += 1
        else:
            a[r] = i
            r -= 1
            m -= 1 << max((n - i - 1), 0)

    a.pop(0)
    print(" ".join(map(str, a)))


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(5)