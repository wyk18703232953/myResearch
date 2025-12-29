import random

def main(n):
    # 随机生成参数 s（题意中是以分钟为单位的间隔）
    # 这里假设 s 在 1~30 之间
    s = random.randint(1, 30)

    # 随机生成 n 个时间点（小时0~23，分钟0~59），并按时间先后排序
    times = []
    for _ in range(n):
        a = random.randint(0, 23)
        b = random.randint(0, 59)
        times.append((a, b))
    times.sort(key=lambda x: x[0] * 60 + x[1])

    # 原代码逻辑封装
    t = [[0, 0]]
    for j in range(n):
        a, b = times[j]
        total = a * 60 + b
        last = t[-1][0] * 60 + t[-1][1] + 1
        t.append([a, b])

        if j == 0:
            if total >= s + 1:
                print(0, 0)
                return

        if total - last > 2 * s:
            u = last + s
            print(u // 60, u % 60)
            return

        if j == n - 1:
            x = t[-1][0] * 60 + t[-1][1]
            print((x + s + 1) // 60, (x + s + 1) % 60)
            return


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)