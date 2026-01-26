def main(n):
    # Generate deterministic weights for n passengers
    ar = [(i * 3 + 1) % (n + 5) + 1 for i in range(n)]

    # Generate deterministic sequence of '0' and '1'
    # Ensure exactly n operations, with number of '0's >= number of '1's at any prefix
    pa = []
    stack_balance = 0
    ones_used = 0
    for i in range(n):
        # Prefer '0' (push) while we still have room
        if stack_balance == 0:
            pa.append(0)
            stack_balance += 1

        else:
            # Alternate deterministically based on index parity
            if (i % 2 == 0) or (n - i <= stack_balance):
                pa.append(1)
                stack_balance -= 1
                ones_used += 1

            else:
                pa.append(0)
                stack_balance += 1

    # Core algorithm from original program
    bus = sorted([(ar[i], i + 1) for i in range(n)])
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
    # print(" ".join(out))
    pass
if __name__ == "__main__":
    main(10)