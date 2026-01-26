def main(n):
    # n controls both number of test cases and array size per test
    # Number of test cases
    T = max(1, n)
    mod = 10**9 + 7

    out_lines = []

    for t in range(1, T + 1):
        # Determine array length for this test case
        a = max(1, n + (t % 5) - 2)

        # Deterministically generate list b of length a
        # Pattern: mix of small repeated values and spread out values
        b = []
        for i in range(a):
            # Mix a periodic small value with a larger varying component
            val = (i % 7) + ((i * (t + 3)) % 11)
            # Keep numbers reasonably small to allow repetitions
            val = val % 20
            b.append(val)

        # Core logic from original program
        w = {}
        for i in range(a):
            key = b[i]
            if key in w:
                w[key] += 1
            else:
                w[key] = 1

        s = -1
        l = 0
        mi = 2325234324324234.0
        d = []

        for i in w:
            if w[i] >= 4:
                t_list = [str(i), str(i), str(i), str(i)]
                out_lines.append(" ".join(t_list))
                l = 1
                break
            if w[i] >= 2:
                d.append(i)

        if l == 1:
            continue

        d.sort()
        p = []
        for i in range(len(d)):
            if s == -1:
                s = d[i]
            else:
                r = float(s) / float(d[i])
                r += float(d[i]) / float(s)
                if r < mi:
                    p = [str(d[i]), str(s)]
                    mi = r
                s = d[i]

        if p:
            p = p * 2
            out_lines.append(" ".join(p))
        else:
            # Fallback if no element repeats at least twice:
            # use first two elements (or duplicate single element) deterministically
            if a == 1:
                val = str(b[0])
                out_lines.append(" ".join([val, val, val, val]))
            else:
                x = str(b[0])
                y = str(b[1])
                out_lines.append(" ".join([x, y, x, y]))

    result = "\n".join(out_lines)
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic runs
    main(5)