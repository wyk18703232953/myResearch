from collections import deque
import random

def main(n):
    # 生成测试数据：根据规模 n 构造 d, k
    # 尝试让构造经常可行：d < n 且 k >= 2
    if n <= 2:
        d = n - 1
        k = 1 if n == 2 else 0
    else:
        d = random.randint(1, max(1, n - 1))
        k = random.randint(2, max(2, n // 2 + 1))

    # 原逻辑开始
    if d + 1 > n:
        print('NO')
        return

    ans = []
    dist = [0] * n
    deg = [0] * n

    # 先构造主链（长度 d 的直径）
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
            print('NO')
            return

    q = deque(list(range(d + 1)))
    cur = d + 1
    while q and cur < n:
        v = q.popleft()
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
        print('NO')
    else:
        print('YES')
        for u, v in ans:
            print(u, v)


# 示例调用
if __name__ == "__main__":
    # 按需要修改 n 来测试
    main(10)