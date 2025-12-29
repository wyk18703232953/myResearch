import random
import heapq

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个权值 w，范围可自行调整
    w = [random.randint(1, 10**6) for _ in range(n)]

    # 生成长度为 2n 的 01 串 s，保证 0 和 1 的数量均为 n
    s_list = ['0'] * n + ['1'] * n
    random.shuffle(s_list)
    s = ''.join(s_list)

    # 2. 原逻辑（移除 input），使用生成的数据 w 和 s

    idx = []
    for i in range(n):
        idx.append((w[i], i + 1))

    idx.sort()
    heapq.heapify(idx)
    ones = []
    heapq.heapify(ones)
    res = []

    for i in range(2 * n):
        if s[i] == '0':
            l = idx[0]
            heapq.heappop(idx)
            res.append(l[1])
            heapq.heappush(ones, [-l[0], l[1]])
        else:
            l = ones[0]
            heapq.heappop(ones)
            res.append(l[1])

    res_str = ' '.join(str(i) for i in res)
    print(res_str)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)