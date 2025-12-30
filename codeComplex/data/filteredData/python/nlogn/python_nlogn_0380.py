import heapq
import random

def main(n):
    # 生成测试数据：n 和 k，以及长度为 n 的两组数组
    # 这里示例生成：
    # k: 0 到 n-1 之间的随机整数
    # pwr_list, cns_list: 1 到 100 之间的随机整数
    if n <= 0:
        return

    k = random.randint(0, max(0, n - 1))
    pwr_list = [random.randint(1, 100) for _ in range(n)]
    cns_list = [random.randint(1, 100) for _ in range(n)]

    # 将原逻辑封装为函数逻辑
    l = sorted(zip(pwr_list, cns_list, range(n)))
    h = []
    sm = 0
    ans = {}

    for i in range(n):
        pwr, cns, ind = l[i]
        sm += cns
        if len(h) > k:
            sm -= heapq.heappop(h)
        ans[ind] = sm
        heapq.heappush(h, cns)

    # 输出结果
    output = " ".join(str(ans[i]) for i in range(n))
    print(output)

# 示例调用
if __name__ == "__main__":
    main(5)