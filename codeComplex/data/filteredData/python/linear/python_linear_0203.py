def main(n):
    # Interpret n as the number of time points
    # Deterministically generate m and the time points
    # m: a fixed positive integer derived from n
    m = max(1, n // 3 + 5)

    b = []
    d = []

    # Generate n deterministic time points (a, c) in non-decreasing order of minutes
    # a: hour, c: minute
    # Ensure times are within a single day (0 <= a < 24, 0 <= c < 60)
    # Construction: base minute t = i * (m + 1) // 2 to allow gaps that may exceed (m*2)+1
    times = []
    for i in range(n):
        t = i * ((m + 1) // 2)
        a = (t // 60) % 24
        c = t % 60
        times.append((a, c))

    for x in range(n):
        a, c = times[x]
        if x == 0:
            if (a * 60) + c > m:
                b.append("0 0")
            d.append((a * 60) + c)

        else:
            if ((a * 60) + c) - d[-1] > (m * 2) + 1:
                f = d[-1] + m + 1
                b.append(str(f // 60) + " " + str((f % 60)))
            d.append((a * 60) + c)

    if len(b) == 0 and len(d) > 0:
        f = d[-1] + m + 1
        b.append(str(f // 60) + " " + str((f % 60)))

    if b:
        # print(b[0])
        pass

    else:
        # Edge case: n == 0, original code assumes at least one line
        # Define a deterministic fallback
        # print("0 0")
        pass
if __name__ == "__main__":
    # Example call for testing; adjust n as needed for experiments
    main(10)