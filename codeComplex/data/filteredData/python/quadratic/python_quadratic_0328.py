import sys
import random


def main(n):
    # 这里根据 n 生成 (d, k) 的测试数据
    # 策略示例：确保有时能构造成功的树，有时失败，便于测试
    if n <= 2:
        d = max(1, n - 1)
        k = 1
    else:
        # 随机生成 d 和 k，但做一些约束以避免明显不合法的情况
        d = random.randint(1, max(1, n - 1))
        k = random.randint(1, max(1, n - 1))

    # 原逻辑开始（移除 input，使用生成的 n, d, k）
    if n <= d:
        print("NO")
        return

    if k == 1 and n > 2:
        print("NO")
        return

    edgestot = []
    edges = [[] for _ in range(n)]
    tovisit = []

    for i in range(d):
        edgestot.append([i, i + 1])
        tovisit.append([i + 1, min(i + 1, d - i - 1)])
        edges[i].append(i + 1)
        edges[i + 1].append(i)

    cur = d + 1
    while cur < n and len(tovisit) > 0:
        x = tovisit.pop()
        if x[1] == 0:
            continue
        while len(edges[x[0]]) < k and cur < n:
            tovisit.append([cur, x[1] - 1])
            edgestot.append([cur, x[0]])
            edges[x[0]].append(cur)
            edges[cur].append(x[0])
            cur += 1

    if len(edgestot) == n - 1:
        print("YES")
        for i in range(n - 1):
            print(edgestot[i][0] + 1, edgestot[i][1] + 1)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时按需要调用 main(n)
    main(10)