from heapq import heappush, heappop

def main(n):
    # n 表示 L 的长度以及字符串 T 的长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成 L：长度为 n，元素为 i % 10 + 1，避免出现 0
    L = [(i % 10) + 1 for i in range(n)]

    # 确定性生成 T：按固定模式在 'G' 和 'W' 间交替
    chars = ['G', 'W']
    T = ''.join(chars[i % 2] for i in range(n))

    ans = sum(L)
    Q = []

    for l, t in zip(L, T):
        if t == 'G':
            heappush(Q, (2, 2 * l))
            heappush(Q, (5, float('inf')))
        elif t == 'W':
            heappush(Q, (1, 2 * l))
            heappush(Q, (3, float('inf')))

        need_stamina = l
        while need_stamina > 0:
            cost, quantity = heappop(Q)
            if need_stamina > quantity:
                ans += quantity * cost
                need_stamina -= quantity

            else:
                ans += need_stamina * cost
                heappush(Q, (cost, quantity - need_stamina))
                need_stamina = 0

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行时间复杂度实验
    main(10)