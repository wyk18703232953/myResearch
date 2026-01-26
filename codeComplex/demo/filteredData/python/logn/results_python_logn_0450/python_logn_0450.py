def main(n):
    # Interpret n as number of test cases and also as parameter scale
    t = n
    outputs = []

    for i in range(t):
        # Deterministically generate (n_i, k_i) from global n and i
        # Ensure n_i >= 1
        ni = max(1, (i % 40) + 1)  # ni in [1, 40]
        # Generate k_i in a range related to ni
        # Use a deterministic polynomial in i to vary k
        base = (i * 7 + 3) * (i + 5)
        ki = base % (1 << max(1, ni))  # keep k in a range dependent on ni

        if ni >= 32:
            outputs.append(f"YES {ni-1}")

        else:
            low = 0
            co = -1
            md = [0]
            for j in range(1, ni):
                md.append(md[-1] * 4 + 1)
            kk = 0
            found = 0
            for cut in range(1, ni + 1):
                low += (1 << cut) - 1
                co = 2 * co + 3
                kk += co * md[ni - cut]
                if ki >= low and ki <= low + kk:
                    outputs.append(f"YES {ni-cut}")
                    found = 1
                    break
            if found == 0:
                outputs.append("NO")

    # Join outputs with newlines for a single print
    # print("\n".join(outputs))
    pass
if __name__ == "__main__":
    main(10)