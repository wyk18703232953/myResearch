def main(n):
    # Deterministic generation of two hidden integers A and B based on n
    # Limit them to 30 bits because the original code loops from bit 29 down to 0
    A = (n * 1234567 + 890123) & ((1 << 30) - 1)
    B = (n * 7654321 + 210987) & ((1 << 30) - 1)

    def oracle(a, b):
        # Simulate the interactive judge:
        # it returns:
        #   -1 if A < B
        #    0 if A == B
        #    1 if A > B
        if A < B:
            return -1
        elif A > B:
            return 1

        else:
            return 0

    # The rest is the original algorithm logic,
    # with input/output replaced by direct calls and local variables.
    cond = oracle(0, 0)
    cur_a = 0
    cur_b = 0
    for i in range(29, -1, -1):
        xor = (1 << i)
        query_a = cur_a ^ xor
        query_b = cur_b ^ xor
        val = oracle(query_a, query_b)
        if val != cond:
            if cond == -1 and val == 1:
                cur_b ^= xor
                query_a = cur_a
                query_b = cur_b
                cond = oracle(query_a, query_b)

            else:
                cur_a ^= xor
                query_a = cur_a
                query_b = cur_b
                cond = oracle(query_a, query_b)

        else:
            cond = val
            query_a = cur_a ^ xor
            query_b = cur_b
            val = oracle(query_a, query_b)
            if val == -1:
                cur_a ^= xor
                cur_b ^= xor

            else:
                pass

    # For experimental purposes, return the discovered (cur_a, cur_b)
    # along with the true (A, B) to allow correctness checking if desired.
    return cur_a, cur_b, A, B


if __name__ == "__main__":
    # Example call for time-complexity experiments
    # You can loop over different n externally.
    result = main(10)
    # print(result)
    pass