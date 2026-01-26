from heapq import *

def main(n):
    # 输入规模映射：
    # n >= 1
    #   实际使用的元素个数为 m = n
    #   k = max(1, n // 3)
    if n <= 0:
        return

    m = n
    k = max(1, n // 3)

    # 生成确定性数据
    # p_vals: 严格递增，方便触发 p[i][0] != p[i-1][0] 的逻辑
    # c_vals: 简单算术构造
    p_vals = [i + 1 for i in range(m)]
    c_vals = [(i * 2 + 3) % (m + 5) for i in range(m)]

    p = [[p_vals[i], c_vals[i], i] for i in range(m)]
    p.sort()
    j = 0
    an = [0] * m
    an[p[0][2]] = p[0][1]
    z = []
    heapify(z)

    for i in range(1, m):
        s = p[i][1]
        if p[i][0] != p[i - 1][0]:
            while j < i:
                heappush(z, -p[j][1])
                j += 1

        tt = []
        for __ in range(k):
            tt.append(heappop(z))
            if not z:
                break
        for v in tt:
            s += abs(v)
            heappush(z, v)
        an[p[i][2]] = s

    # print(*an)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)