import bisect
import random

def max_eligible(a, x):
    ind = bisect.bisect_right(a, x)
    if ind <= len(a):
        return a[ind - 1]
    else:
        return -1

def main(n):
    # 生成测试数据：
    # 1. 随机生成一个递增数组 a，长度为 n
    # 2. 随机生成 U，使得有一定概率能取到有意义的结果
    if n < 3:
        print(-1)
        return

    # 生成递增数组 a
    a = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)  # 间隔为 1~10 的递增
        a.append(cur)

    # 生成 U（相对数组范围的随机值）
    U = random.randint(1, max(1, (a[-1] - a[0]) // 2))

    max_val = -1
    for i in range(n - 2):
        x = a[i] + U
        val1 = max_eligible(a, x)

        if val1 != -1 and val1 != a[i + 1] and val1 != a[i]:
            val = (val1 - a[i + 1]) / (val1 - a[i])
            if val > max_val:
                max_val = val

    print(max_val)

if __name__ == "__main__":
    # 可以在这里调整 n 的规模进行测试
    main(10)