def main(n):
    # Interpret n as the number of time points (the original 'n')
    # Fixed s for determinism and scalability behavior; can be tuned if needed
    s = max(1, n // 3)

    # Deterministic generation of n (hour, minute) pairs
    # Ensure times are non-decreasing in minutes
    times = []
    current_minutes = 0
    for i in range(n):
        # Step in minutes grows slowly with i to avoid enormous jumps
        step = 1 + (i % 5)
        current_minutes += step
        hour = (current_minutes // 60) % 24
        minute = current_minutes % 60
        times.append((hour, minute))

    t = [[0, 0]]
    for j in range(n):
        a, b = times[j]
        total = a * 60 + b
        last = t[-1][0] * 60 + t[-1][1] + 1
        t.append([a, b])

        if j == 0:
            if total >= s + 1:
                # print(0, 0)
                pass
                break

        if total - last > 2 * s:
            u = last + s
            # print(u // 60, u % 60)
            pass
            break

        if j == n - 1:
            x = t[-1][0] * 60 + t[-1][1]
            # print((x + s + 1) // 60, (x + s + 1) % 60)
            pass
            break


if __name__ == "__main__":
    # Example invocation; adjust n as needed for experiments
    main(10)