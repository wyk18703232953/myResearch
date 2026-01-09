def main(n):
    # In the original interactive problem, there is a hidden pair (A, B)
    # and queries of the form f(x, y) = sign((A ^ x) - (B ^ y)) are answered:
    #   -1 if (A ^ x) < (B ^ y)
    #    0 if (A ^ x) == (B ^ y)
    #    1 if (A ^ x) > (B ^ y)
    #
    # This reconstruction makes everything deterministic and non-interactive.
    # We:
    #   - deterministically generate A, B from n
    #   - simulate the query-answer mechanism with a local function
    #   - run the original bitwise reconstruction algorithm
    #   - return (cur_a, cur_b) to match the inferred pair
    
    # Map n to hidden A, B deterministically.
    # Use at most 30 bits, since original code loops i in range(29, -1, -1).
    # Simple deterministic constructions:
    A = (n * 1234567) & ((1 << 30) - 1)
    B = (n * 7654321 + 1) & ((1 << 30) - 1)

    def query(x, y):
        ax = A ^ x
        by = B ^ y
        if ax < by:
            return -1
        elif ax > by:
            return 1

        else:
            return 0

    # Simulate the original interactive protocol
    cond = query(0, 0)
    cur_a = 0
    cur_b = 0
    for i in range(29, -1, -1):
        xor = 1 << i
        query_a = cur_a ^ xor
        query_b = cur_b ^ xor
        val = query(query_a, query_b)
        if val != cond:
            if cond == -1 and val == 1:
                cur_b ^= xor
                query_a = cur_a
                query_b = cur_b
                val = query(query_a, query_b)
                cond = val

            else:
                cur_a ^= xor
                query_a = cur_a
                query_b = cur_b
                val = query(query_a, query_b)
                cond = val

        else:
            cond = val
            query_a = cur_a ^ xor
            query_b = cur_b
            val = query(query_a, query_b)
            if val == -1:
                cur_a ^= xor
                cur_b ^= xor

            else:
                pass

    # For experiments, we return the reconstructed values.
    # This keeps the computation deterministic and scalable in terms of bit-length.
    return cur_a, cur_b


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    n = 10
    a, b = main(n)
    # print(a, b)
    pass