from collections import deque
import random


def solve(n, d, k):
    if n == 1 or n <= d:
        ans = "NO"
        edges = []
    elif k == 1:
        ans = "YES" if n == 2 and d == 1 else "NO"
        edges = [(1, 2)] if ans == "YES" else []
    else:
        edges = [(i + 1, i + 2) for i in range(d)]
        q = deque()
        l, r = 1, d + 1
        if k > 2:
            for i in range(2, d + 1):
                # item: (node, depth_from_root, remaining_radius)
                q.append((i, 2, min(i - l, r - i)))
        ans = "YES"
        for i in range(d + 2, n + 1):
            if not q:
                ans = "NO"
                break
            j, k0, d0 = q.popleft()
            edges.append((j, i))
            if k0 + 1 < k:
                q.append((j, k0 + 1, d0))
            if d0 - 1 > 0:
                q.append((i, 1, d0 - 1))
    return ans, edges


def gen_test_data(n):
    # 简单根据 n 构造一组 (n, d, k) 以触发不同分支
    if n <= 2:
        # 小规模时，随便选一个合法 d,k 范围
        d = 1 if n == 2 else 0
        k = 1
    else:
        # 随机在合理范围内生成 d,k
        d = random.randint(1, max(1, n - 1))
        k = random.randint(1, max(1, n // 2))
    return n, d, k


def main(n):
    n, d, k = gen_test_data(n)
    ans, edges = solve(n, d, k)
    print(ans)
    if ans == "YES":
        for u, v in edges:
            print(u, v)


if __name__ == "__main__":
    # 示例：可以在这里手动调用 main 进行简单测试
    main(10)