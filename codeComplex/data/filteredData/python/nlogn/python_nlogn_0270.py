import random

def main(n):
    # 生成测试数据：n 行，每行两个整数 [l, r]
    # 这里生成保证 l <= r，范围可按需要调整
    a = []
    for _ in range(n):
        l = random.randint(0, 10**5)
        r = random.randint(l, l + random.randint(0, 10**5))
        a.append([l, r])

    # 原逻辑开始
    for t in range(n):
        a[t].append(t + 1)  # 记录原下标(从1开始)

    a.sort()  # 按 [l, r, idx] 的字典序排序

    for i in range(n - 1):
        if a[i][1] >= a[i + 1][1]:
            print(a[i + 1][2], a[i][2])
            return
        if a[i][0] == a[i + 1][0] and a[i][1] <= a[i + 1][1]:
            print(a[i][2], a[i + 1][2])
            return

    print(-1, -1)


if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(5)