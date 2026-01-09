from collections import deque

def main(n):
    # 解释输入结构：
    # 原程序读取：n, m, k 和一个长度为 m 的数组
    # 这里将 n 作为数组长度 m，同时令原来的 n = m，k = max(1, n // 3)
    # 为了保证行为合理，构造一个递增数组 a，元素值从 1 开始，步长为 2
    m = n
    if m <= 0:
        # print(0)
        pass
        return

    orig_n = m
    k = max(1, m // 3)

    a = deque(1 + 2 * i for i in range(m))

    oper = 0
    rem = 0
    while a:
        x = a.popleft()
        pg = (x - 1 - rem) // k
        lrem = 1
        while a and (a[0] - 1 - rem) // k == pg:
            a.popleft()
            lrem += 1
        rem += lrem
        oper += 1
    # print(oper)
    pass
if __name__ == "__main__":
    main(10)