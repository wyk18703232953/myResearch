import random

def main(n):
    # 随机生成参数 s（等待时间），范围 0~59 分钟
    s = random.randint(0, 59)

    # 生成 n 个时间点（小时、分钟），按分钟递增排序，范围 0:00 ~ 23:59
    times = sorted(random.sample(range(0, 24 * 60), k=n))

    a = times[:]  # 直接使用分钟表示的时间数组

    if a[0] != 0 and a[0] > s:
        print(0, 0)
    else:
        a.append(a[n - 1] + 2 * s + 3)
        for i in range(1, n + 1):
            if a[i] - (a[i - 1] + 2 + s) >= s:
                t = a[i - 1] + s + 1
                print(t // 60, t % 60)
                break


if __name__ == "__main__":
    # 示例：调用 main，规模为 5
    main(5)