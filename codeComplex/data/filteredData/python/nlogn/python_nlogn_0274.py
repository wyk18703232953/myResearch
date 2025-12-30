import random

def main(n):
    # 生成测试数据：n 个区间 (l, r)，保证 l <= r
    intervals = []
    for i in range(1, n + 1):
        l = random.randint(0, 10 * n)
        r = random.randint(l, l + 10 * n)
        intervals.append((l, r, i))

    # 模拟原始代码逻辑
    a = intervals[:]  # 拷贝一份，避免修改原数据
    a.sort()

    for i in range(n - 1):
        if a[i][0] == a[i + 1][0]:
            print(str(a[i][2]) + ' ' + str(a[i + 1][2]))
            break

        if a[i][1] >= a[i + 1][1]:
            print(str(a[i + 1][2]) + ' ' + str(a[i][2]))
            break
    else:
        print('-1 -1')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)