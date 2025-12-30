import random

def main(n):
    # 生成测试数据
    # 约束：1 <= k <= n
    k = random.randint(1, n)
    # 生成 a, t 数组
    # a 为正整数，范围可自行调整
    a = [random.randint(0, 10) for _ in range(n)]
    # t 为 0/1
    t = [random.randint(0, 1) for _ in range(n)]

    x = 0
    summ = 0
    maxx = 0

    # 原逻辑：计算基础已清醒部分
    for i in range(n):
        summ += a[i] * t[i]

    # 初始窗口 [0, k-1] 中通过"叫醒"增加的值
    for i in range(k):
        if not t[i]:
            x += a[i]
    maxx = max(maxx, x)

    # 滑动窗口，窗口大小为 k
    for i in range(n - k):
        # 进入窗口的元素：i+k
        x += a[i + k] * (1 - t[i + k])
        # 离开窗口的元素：i
        x -= a[i] * (1 - t[i])
        if x > maxx:
            maxx = x

    result = summ + maxx
    print("n =", n)
    print("k =", k)
    print("a =", a)
    print("t =", t)
    print("result =", result)
    return result

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)