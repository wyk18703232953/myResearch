def main(n):
    # In the original interactive problem, the judge had two hidden integers A and B,
    # and answered queries of the form "? x y" with sign(A - B) relative to (x, y).
    # For determinism, we construct fixed A, B from n and simulate the judge.
    # Let A and B be 30-bit numbers derived deterministically from n.
    A = (n * 1234567) & ((1 << 30) - 1)
    B = (n * 7654321 + 42) & ((1 << 30) - 1)

    def judge(x, y):
        if (A ^ x) > (B ^ y):
            return '1'
        elif (A ^ x) < (B ^ y):
            return '-1'

        else:
            return '0'

    # Simulate the interactive algorithm
    res = judge(0, 0)
    a = 0
    b = 0
    for i in range(29, -1, -1):
        res1 = judge(a ^ (1 << i), b)
        res2 = judge(a, b ^ (1 << i))
        if res1 == res2:
            if res == '1':
                a ^= (1 << i)

            else:
                b ^= (1 << i)
            res = res1
        elif res1 == '-1':
            a ^= (1 << i)
            b ^= (1 << i)

    # For experiment purposes, return the reconstructed a, b and the original A, B
    return a, b, A, B


if __name__ == "__main__":
    # Example deterministic call for scalability experiments
    result = main(10)
    # print(result)
    pass