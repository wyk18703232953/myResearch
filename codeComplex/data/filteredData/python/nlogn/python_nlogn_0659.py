from heapq import heappush, heappop
import random

def main(n: int) -> int:
    # 1. 生成测试数据
    # L: n个正整数，代表每段需要的体力
    # T: 长度为n的字符串，由 'G' 和 'W' 组成
    random.seed(0)
    L = [random.randint(1, 10) for _ in range(n)]
    T = ''.join(random.choice('GW') for _ in range(n))

    # 2. 原始逻辑
    # fly -> walk, time cost: +4s, stamina: +2
    # walk in place, time cost: +5s, stamina: +1

    # fly -> swim, time cost: +2s, stamina: +2
    # swim in place, time cost: +3s, stamina:+1

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
                if quantity - need_stamina > 0:
                    heappush(Q, (cost, quantity - need_stamina))
                need_stamina = 0

    return ans


if __name__ == "__main__":
    # 示例：n=5
    print(main(5))