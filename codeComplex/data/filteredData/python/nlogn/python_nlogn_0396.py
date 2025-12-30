import heapq
import random

def main(n):
    # 生成测试数据
    # 约定：k 在 [0, n] 范围内
    k = random.randint(0, n)
    # 生成 p 为 0~10^9 的随机整数
    p = [random.randint(0, 10**9) for _ in range(n)]
    # 生成 c 为 0~10^9 的随机整数
    c = [random.randint(0, 10**9) for _ in range(n)]

    indexes = sorted(list(range(n)), key=p.__getitem__)
    most_vyg_odn_yye = []
    res = [1] * n
    cur_res = 0

    for ind in indexes:
        this_cost = c[ind]
        heapq.heappush(most_vyg_odn_yye, this_cost)
        cur_res += this_cost
        res[ind] = cur_res
        if len(most_vyg_odn_yye) > k:
            cur_res -= heapq.heappop(most_vyg_odn_yye)

    print(*res)


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)