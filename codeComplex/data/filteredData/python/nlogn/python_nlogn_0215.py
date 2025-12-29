import random

def sss(a, l, r, tt, m):
    f = -1
    while l <= r:
        mid = (l + r) >> 1
        if a[mid] - a[tt] <= m:
            f = mid
            l = mid + 1
        else:
            r = mid - 1
    return f

def main(n):
    # 生成测试数据
    # 保证有序数组 a，方便使用二分逻辑
    # a 为递增序列，差值在 1~10 之间
    a = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)
        a.append(cur)
    # 生成 m，控制在数组跨度范围内
    m = random.randint(1, max(1, a[-1] - a[0]))

    l = len(a)
    Maxx = -1.0
    for i in range(0, l - 2):
        if a[i + 2] - a[i] <= m:
            k = sss(a, i + 2, l - 1, i, m)
            if k != -1:
                Maxx = max(Maxx, (a[k] - a[i + 1]) / (a[k] - a[i]))

    if Maxx == -1:
        print(-1)
    else:
        print(f"{Maxx:.15f}")

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)