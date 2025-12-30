# Converted version of "Bus of Characters"
# - No input()
# - Logic wrapped in main(n)
# - Test data auto-generated from n

import random

def main(n: int):
    # 1. Generate test data based on n
    # Generate passenger weights (or arbitrary positive integers)
    # Here: distinct random weights between 1 and 10^9
    ar = random.sample(range(1, 10**9), n)

    # Generate sequence of 0/1 of length 2n with exactly n zeros and n ones
    pa = [0] * n + [1] * n
    random.shuffle(pa)

    # 2. Original algorithm logic
    bus = sorted((ar[i], i + 1) for i in range(n))
    seq = []
    tail = 0
    out = []

    for p in pa:
        if p == 0:
            out.append(str(bus[tail][1]))
            seq.append(tail)
            tail += 1
        else:
            v = seq.pop()
            out.append(str(bus[v][1]))

    # 3. Output in the same format as original code
    print(" ".join(out))


if __name__ == "__main__":
    # Example: run with some n
    main(5)