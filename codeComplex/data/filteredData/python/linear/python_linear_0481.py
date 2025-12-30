import random


def main(n: int):
    # 生成测试数据：n 个区间 [l, r]，保证 l <= r
    # 范围可根据需要调整，这里用 [0, 10^6]
    t = n
    tup = []
    for _ in range(t):
        a = random.randint(0, 10**6)
        b = random.randint(0, 10**6)
        l, r = (a, b) if a <= b else (b, a)
        tup.append([l, r])

    # 原逻辑开始
    tup.sort()
    l = tup[0][0]
    r = tup[0][1]
    prefix = [[l, r]]
    for i in range(1, t):
        if l > tup[i][1] or r < tup[i][0]:
            prefix.append([-1, -1])
            for _ in range(i + 1, t):
                prefix.append([-1, -1])
            break

        l = max(l, tup[i][0])
        r = min(r, tup[i][1])
        prefix.append([l, r])

    l = tup[-1][0]
    r = tup[-1][1]
    suffix = [[-1, -1] for _ in range(t)]
    suffix[-1][0] = l
    suffix[-1][1] = r
    for i in range(t - 2, -1, -1):
        if l > tup[i][1] or r < tup[i][0]:
            break

        l = max(l, tup[i][0])
        r = min(r, tup[i][1])
        suffix[i][0] = l
        suffix[i][1] = r

    ans = 0
    if t == 1:
        # 特殊情况：只有一个区间，等价于删除它后无区间，答案为 0
        print(0)
        return

    for i in range(t):
        if i == 0:
            ans = max(ans, abs(suffix[i + 1][0] - suffix[i + 1][1]))
            continue
        if i == t - 1:
            ans = max(ans, abs(prefix[i - 1][0] - prefix[i - 1][1]))
            continue
        prefix_l = prefix[i - 1][0]
        prefix_r = prefix[i - 1][1]
        suffix_l = suffix[i + 1][0]
        suffix_r = suffix[i + 1][1]
        l = max(prefix_l, suffix_l)
        r = min(prefix_r, suffix_r)
        ans = max(ans, max(0, r - l))
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)