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
    # 生成测试数据：
    # 1. 生成一个递增数组 a，长度为 n
    # 2. 生成一个正整数 m
    if n < 3:
        print(-1)
        return

    # 生成递增数组 a
    a = []
    cur = 0
    for _ in range(n):
        cur += random.randint(1, 10)
        a.append(cur)

    # 生成 m，使得有一定概率存在满足条件的三元组
    # m 取为数组整体跨度的一部分
    m = max(1, (a[-1] - a[0]) // 3)

    Maxx = -1.0
    l = len(a)

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