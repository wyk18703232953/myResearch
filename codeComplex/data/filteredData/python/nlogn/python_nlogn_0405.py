import random

def main(n):
    # 生成测试数据：n 个区间 [x, y]，保证 x <= y
    intervals = []
    for _ in range(n):
        x = random.randint(0, 10 * n)
        y = random.randint(x, x + 10 * n)
        intervals.append((x, y))

    # 原逻辑开始
    a = []
    for x, y in intervals:
        a.append((x, 0))
        a.append((y, 1))
    a.sort()

    ans, s = [0] * n, []
    for x, y in a:
        if y:
            ans[len(s) - 1] += x - s[-1][0] + 1 - s[-1][1]
            z = s.pop()
            if s:
                s[-1][1] += (x - z[0] + 1)
        else:
            s.append([x, 0])

    print(*ans)
    return ans, intervals


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)