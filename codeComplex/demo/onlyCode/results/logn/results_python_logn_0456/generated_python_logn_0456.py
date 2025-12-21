def main(n):
    import random
    def judge(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    A = random.randint(0, (1 << n) - 1)
    B = random.randint(0, (1 << n) - 1)
    def ip_sim(query_a, query_b):
        return judge(A ^ query_a, B ^ query_b)
    t = 1
    results = []
    for _ in range(t):
        cur_a = 0
        cur_b = 0
        cond = ip_sim(0, 0)
        for i in range(n - 1, -1, -1):
            xor = 1 << i
            query_a = cur_a ^ xor
            query_b = cur_b ^ xor
            val = ip_sim(query_a, query_b)
            if val != cond:
                if cond == -1 and val == 1:
                    cur_b ^= xor
                    cond = ip_sim(cur_a, cur_b)
                else:
                    cur_a ^= xor
                    cond = ip_sim(cur_a, cur_b)
            else:
                cond = val
                query_a = cur_a ^ xor
                query_b = cur_b
                val = ip_sim(query_a, query_b)
                if val == -1:
                    cur_a ^= xor
                    cur_b ^= xor
        results.append((cur_a, cur_b, A, B))
    return results
if __name__ == "__main__":
    print(main(30))