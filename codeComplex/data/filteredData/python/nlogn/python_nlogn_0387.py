import heapq
import random

def Solution(td, n, k):
    mxHeap = []
    td = sorted(td, key=lambda x: x[0])
    prefix = []
    tmp = 0
    for v in td:
        b = v[1]
        tmpAns = tmp + b
        if len(mxHeap) == k:
            if len(mxHeap) and b > mxHeap[0]:
                t = heapq.heappop(mxHeap)
                heapq.heappush(mxHeap, b)
                tmp -= t
                tmp += b
        elif len(mxHeap) < k:
            tmp += b
            heapq.heappush(mxHeap, b)
        prefix.append([tmpAns, v[2]])

    ans = [0 for _ in range(n)]
    for v in prefix:
        ans[v[1]] = v[0]
    print(*ans)


def main(n):
    # 生成规模为 n 的测试数据
    random.seed(0)
    k = random.randint(1, n)  # 1 <= k <= n
    a = [random.randint(1, 10**6) for _ in range(n)]
    b = [random.randint(1, 10**6) for _ in range(n)]
    td = [[a[i], b[i], i] for i in range(n)]
    Solution(td, n, k)


if __name__ == '__main__':
    # 示例：可根据需要修改 n 的值进行测试
    main(5)