def main(n):
    # Deterministically generate hidden numbers a0 and b0 from n
    # so that the behavior is completely deterministic and scalable.
    # We limit to 30 bits as in the original code.
    a0 = (n * 1234567) & ((1 << 30) - 1)
    b0 = (n * 8901234 + 7) & ((1 << 30) - 1)

    # Oracle function: replicates the interactive judge behavior
    # Returns:
    #   '1'  if (a ^ a0) > (b ^ b0)
    #   '-1' if (a ^ a0) < (b ^ b0)
    #   '0'  if equal (though original logic never expects '0')
    def oracle(a, b):
        va = a ^ a0
        vb = b ^ b0
        if va > vb:
            return '1'
        elif va < vb:
            return '-1'

        else:
            return '0'

    # Simulate the original interactive logic
    res = oracle(0, 0)
    a = 0
    b = 0
    for i in range(29, -1, -1):
        res1 = oracle(a ^ (1 << i), b)
        res2 = oracle(a, b ^ (1 << i))
        if res1 == res2:
            if res == '1':
                a ^= (1 << i)

            else:
                b ^= (1 << i)
            res = res1
        elif res1 == '-1':
            a ^= (1 << i)
            b ^= (1 << i)

    # For experiment consistency, return both the reconstructed (a, b)
    # and the true hidden (a0, b0)
    return a, b, a0, b0


if __name__ == "__main__":
    # Example deterministic call for experimentation
    result = main(10)
    # print(result)
    pass