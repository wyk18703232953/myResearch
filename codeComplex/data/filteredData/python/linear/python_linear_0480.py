import random

def main(n):
    # 生成测试数据：n 个区间 [l, r]，保证 l <= r
    # 范围可根据需要调整，这里使用 [-10^9, 10^9]
    LIM = 10**9
    z = []
    for _ in range(n):
        l = random.randint(-LIM, LIM)
        r = random.randint(l, LIM)
        z.append([l, r])

    def intersection(l1, r1, l2, r2):
        if l1 > r2 or r1 < l2:
            return [0, 0]
        else:
            return [max(l1, l2), min(r1, r2)]

    # 原代码假定 n >= 2，若 n < 2 时长度为 0
    if n <= 1:
        print(0)
        return

    pref = []
    suff = []

    # 初始化前缀、后缀区间
    pix, piy = intersection(z[0][0], z[0][1], z[0][0], z[0][1])
    six, siy = intersection(z[-1][0], z[-1][1], z[-1][0], z[-1][1])

    for i in range(n):
        pix, piy = intersection(pix, piy, z[i][0], z[i][1])
        pref.append([pix, piy])

    for i in range(n - 1, -1, -1):
        six, siy = intersection(six, siy, z[i][0], z[i][1])
        suff.append([six, siy])
    suff = suff[::-1]

    # 去掉一个区间后的最大交集长度
    ans = max(suff[1][1] - suff[1][0], pref[n - 2][1] - pref[n - 2][0])
    for i in range(1, n - 1):
        inter = intersection(pref[i - 1][0], pref[i - 1][1],
                             suff[i + 1][0], suff[i + 1][1])
        ans = max(ans, inter[1] - inter[0])

    print(ans)


if __name__ == "__main__":
    # 示例调用：规模 n = 5
    main(5)