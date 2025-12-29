from collections import deque
import random

INF = 1000_000_000


def solve_single_case(n, q, arr, queries):
    maxval = max(arr)
    d = deque(arr)
    ans = {}
    count = 1

    # 模拟直到最大值到达队首
    while d[0] != maxval:
        a = d.popleft()
        b = d.popleft()
        ans[count] = (a, b)
        count += 1
        if a > b:
            d.append(b)
            d.appendleft(a)
        else:
            d.append(a)
            d.appendleft(b)

    # 后续循环中最大值固定在队首，剩余元素形成周期
    cycle_len = n - 1
    results = []
    for m in queries:
        if m in ans:
            results.append(ans[m])
        else:
            idx = (m - count) % cycle_len  # 0-based index in cycle
            results.append((maxval, d[1 + idx]))
    return results


def main(n):
    # 生成一组测试数据，规模由 n 控制
    # 这里令数组长度为 n，最大查询次数也为 n
    if n <= 1:
        n = 2

    # 随机生成数组，保证元素互不相同，范围 [1, 2n]
    # 为了稳定，可以固定种子
    random.seed(0)
    arr = random.sample(range(1, 2 * n + 1), n)

    # 生成 q 个随机查询，范围在 [1, 2n] 内
    q = n
    queries = [random.randint(1, 2 * n) for _ in range(q)]

    # 求解并输出
    results = solve_single_case(n, q, arr, queries)
    for a, b in results:
        print(a, b)


if __name__ == "__main__":
    # 示例：可以在此调整 n 测试
    main(5)