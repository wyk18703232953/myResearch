from collections import deque
import random


def solve(n, d, k):
    if d + 1 > n:
        return False, []

    ans = []
    dist = [0] * n
    deg = [0] * n

    # 构造主链
    for i in range(d + 1):
        if i == 0 or i == d:
            deg[i] = 1
        else:
            deg[i] = 2
        if i != d:
            ans.append((i + 1, i + 2))
        dist[i] = max(i, d - i)

    for i in range(n):
        if deg[i] > k:
            return False, []

    q = deque(range(d + 1))
    cur = d + 1
    while q and cur < n:
        v = q.pop()
        if dist[v] < d and deg[v] < k:
            deg[v] += 1
            dist[cur] = dist[v] + 1
            deg[cur] = 1
            ans.append((v + 1, cur + 1))
            q.append(v)
            q.append(cur)
            cur += 1
        else:
            continue

    if cur != n:
        return False, []
    return True, ans


def gen_test_params(n):
    # 简单的可调测试数据生成策略：
    # 1) 让 d 在 [1, n-1] 内随机（或固定规则）
    # 2) 让 k 至少为 1，适当偏大以增加构造成功概率
    if n < 2:
        # 对于 n < 2，原算法无意义，这里给出退化参数
        return 1, 1

    # 示例策略：d 接近 log2(n) 或随机
    d = min(max(1, int(n ** 0.5)), n - 1)
    # k 至少为 2，且不超过 n-1
    k = min(max(2, int((n - 1) ** 0.5) + 1), n - 1)

    # 偶尔随机扰动一下
    if n > 5 and random.random() < 0.3:
        d = random.randint(1, n - 1)
    if n > 5 and random.random() < 0.3:
        k = random.randint(1, n - 1)

    return d, k


def main(n: int):
    # 根据规模 n 生成一组 (d, k)
    d, k = gen_test_params(n)

    ok, edges = solve(n, d, k)

    if not ok:
        print("NO")
        return

    print("YES")
    for u, v in edges:
        print(u, v)


if __name__ == "__main__":
    # 示例：可在此处调用 main 进行本地测试
    # main(10)
    pass