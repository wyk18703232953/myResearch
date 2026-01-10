import heapq

def main(n):
    # n: problem size, also used as k for determinism and scalability
    if n <= 0:
        return

    # Deterministic generation of inputs
    # p: permutation-like but deterministic via simple formula
    p = [(i * 3 + 1) % n for i in range(n)]
    # c: deterministic costs
    c = [(i * 7 + 5) % (2 * n + 1) for i in range(n)]
    k = n // 2  # scale k with n in a deterministic way

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
    main(10)