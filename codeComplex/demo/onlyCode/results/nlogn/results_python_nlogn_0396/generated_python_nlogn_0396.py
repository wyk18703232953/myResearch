import heapq
import random

def main(n):
    k = max(0, n // 2)
    p = list(range(n))
    random.shuffle(p)
    c = [random.randint(1, 100) for _ in range(n)]
    indexes = sorted(list(range(n)), key=p.__getitem__)
    most_vyg_odn_yye = []
    res = [1]*n
    cur_res = 0
    for ind in indexes:
        this_cost = c[ind]
        heapq.heappush(most_vyg_odn_yye, this_cost)
        cur_res += this_cost
        res[ind] = cur_res
        if len(most_vyg_odn_yye) > k:
            cur_res -= heapq.heappop(most_vyg_odn_yye)
    print(*res)
    return res

if __name__ == "__main__":
    main(10)