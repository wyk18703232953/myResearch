from heapq import heapify, heappush, heappop
import random


def main(n, k=None, seed=0):
    """
    参数
    ----
    n : int
        规模（元素个数）
    k : int, 可选
        每次从堆中取出的个数，默认取 min(5, n)
    seed : int
        随机种子，保证复现
    """
    if k is None:
        k = min(5, n)

    random.seed(seed)

    # 生成测试数据：
    # p[i] 为某种“位置”，允许重复；c[i] 为正费用
    # 保持与原代码语义一致：p 是 int 列表，c 是 int 列表
    p = [random.randint(1, max(1, n // 2)) for _ in range(n)]
    c = [random.randint(1, 100) for _ in range(n)]

    # 以下保持原逻辑
    arr = [[p[i], c[i], i] for i in range(n)]
    arr.sort()
    j = 0
    an = [0] * n
    an[arr[0][2]] = arr[0][1]
    z = []
    heapify(z)

    for i in range(1, n):
        s = arr[i][1]
        if arr[i][0] != arr[i - 1][0]:
            while j < i:
                heappush(z, -arr[j][1])
                j += 1

        tt = []
        for __ in range(k):
            if not z:
                break
            tt.append(heappop(z))

        for v in tt:
            s += abs(v)
            heappush(z, v)

        an[arr[i][2]] = s

    # 输出结果
    print(*an)


if __name__ == "__main__":
    # 示例：n=10
    main(10)