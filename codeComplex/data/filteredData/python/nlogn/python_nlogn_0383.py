import heapq
import random

def main(n):
    # 生成测试数据
    # k 在 [0, n] 范围内
    k = random.randint(0, n)
    # P 生成为 1..n 的随机排列（或任意整数序列都可以）
    P = list(range(n))
    random.shuffle(P)
    # C 生成为 1..10 的随机权值（可按需调整范围）
    C = [random.randint(1, 10) for _ in range(n)]

    # 以下为原逻辑，仅移除 input，封装成 main(n)
    Q = []
    for i, p in enumerate(P):
        Q.append((p, i))
    Q.sort()
    q = []
    heapq.heapify(q)
    s = 0
    ans = [0] * n

    if k > 0:
        for p, i in Q:
            ans[i] = s + C[i]
            if len(q) == k:
                if q[0] <= C[i]:
                    v = heapq.heappop(q)
                    heapq.heappush(q, C[i])
                    s -= v
                    s += C[i]
            else:
                heapq.heappush(q, C[i])
                s += C[i]
    else:
        for p, i in Q:
            ans[i] = C[i]

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)