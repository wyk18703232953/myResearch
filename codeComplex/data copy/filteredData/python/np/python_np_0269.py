def setting(s):
    if s == '0':
        return -1
    i = len(s) - 1
    cc = 0
    while i >= 0 and s[i] == '0':
        cc += 1
        i -= 1
    return cc

def process_query(n, v, ops):
    # x is based on n in the original code
    x = len(bin(n)[2:]) - 1
    for j in ops:
        temp = bin(v)[2:]
        abe = setting(temp)
        if j == "U":
            if abe >= x:
                continue
            p = v + (1 << abe)
            n2 = v - (1 << abe)
            x1 = setting(bin(p)[2:])
            x2 = setting(bin(n2)[2:])  # kept for consistency, though unused
            if x1 == abe + 1:
                v = p

            else:
                v = n2
        elif j == "L":
            if abe <= 0:
                continue
            v = v - (1 << (abe - 1))
        else:  # 'R' or any other non 'U'/'L' character
            if abe <= 0:
                continue
            v = v + (1 << (abe - 1))
    return v

def main(n):
    """
    n: problem scale, used to generate deterministic test data.

    We will generate:
      - q = n queries
      - For each query i (1-based):
          v_i = i
          ops_i: a deterministic pattern over 'U', 'L', 'R'
    The function prints the answers, one per line, just like the original code.
    """
    q = n

    # Deterministic generation of test data based on n
    ops_chars = ['U', 'L', 'R']
    results = []
    for i in range(1, q + 1):
        v = i
        # length of operations sequence grows slowly with i to keep it reasonable
        length = max(1, (i % 7) + 1)
        ops = ''.join(ops_chars[(i + k) % 3] for k in range(length))
        res = process_query(n, v, ops)
        results.append(res)

    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # Example: run main with some scale, e.g., n = 10
    main(10)