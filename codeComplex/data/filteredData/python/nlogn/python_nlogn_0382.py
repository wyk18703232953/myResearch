import random
from heapq import heappush, heappop


def main(n):
    # 生成测试数据
    # 约束：k 范围 [0, n]，p、c 为非负整数
    if n <= 0:
        return

    # 生成随机 p 和 c，保持与原逻辑兼容
    plst = [random.randint(0, 10) for _ in range(n)]
    clst = [random.randint(0, 10) for _ in range(n)]
    k = random.randint(0, n)

    if k == 0:
        print(*clst)
        return

    pc = sorted(
        ((p, c, i) for i, (p, c) in enumerate(zip(plst, clst))),
        key=lambda t: (t[0], t[2])
    )
    res = [0] * n
    pq = []
    pq_sum = 0
    pq_size = 0

    for p, c, i in pc:
        if i > 0 and plst[i] == plst[i - 1]:
            res[i] = res[i - 1]
        else:
            res[i] = pq_sum + c

        if pq_size < k:
            heappush(pq, c)
            pq_sum += c
            pq_size += 1
        else:
            alt = heappop(pq)
            if alt < c:
                heappush(pq, c)
                pq_sum += c - alt
            else:
                heappush(pq, alt)

    print(*res)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模
    main(10)