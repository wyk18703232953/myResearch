from heapq import heappush, heappop
import random

def main(n):
    # 生成测试数据
    # k 为 [0, n] 之间的随机整数
    k = random.randint(0, n)
    # powers 和 coins 为 1 到 100 之间的随机整数
    powers = [random.randint(1, 100) for _ in range(n)]
    coins = [random.randint(1, 100) for _ in range(n)]

    A = []
    ans = [0] * n
    for i in range(n):
        A.append((powers[i], coins[i], i))
    A.sort()
    h = []
    total = 0
    for i in range(n):
        _, c, idx = A[i]
        ans[idx] = total + c
        if len(h) < k:
            heappush(h, c)
            total += c
        elif h and h[0] < c:
            total -= heappop(h)
            heappush(h, c)
            total += c

    for x in ans:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)