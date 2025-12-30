import sys
import heapq
import random

def main(n):
    # 生成测试数据：n个正整数，k 为 1~n 之间的随机值
    random.seed(0)
    arr = [random.randint(1, 100) for _ in range(n)]
    k = random.randint(1, n)

    q = []
    for i in range(n):
        heapq.heappush(q, (-arr[i], i))

    res = []
    temp_k = k
    while temp_k:
        val, idx = heapq.heappop(q)
        res.append((-val, idx))
        temp_k -= 1

    res.sort(key=lambda x: x[1])

    ans = 0
    for v, _ in res:
        ans += v

    path = []
    cnt = 0
    for i in range(n):
        if (arr[i], i) in res:
            path.append(cnt + 1)
            cnt = 0
        else:
            cnt += 1
    path[-1] += n - sum(path)

    print(ans)
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)