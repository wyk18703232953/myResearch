def main(n):
    # Interpret n as: number of times; s is derived deterministically from n
    # Generate s deterministically
    s = n // 3

    times = []
    result = 0
    need = True

    # Deterministically generate n time points (h, m)
    # Pattern: i-th time is at minute (i * (s + 2)) modulo 1440, sorted
    for i in range(n):
        total_minutes = (i * (s + 2)) % (24 * 60)
        h = total_minutes // 60
        m = total_minutes % 60
        times.append(60 * h + m)

    times.sort()

    if n == 1:
        if 0 + s + 1 <= times[0]:
            need = False

    for i in range(n - 1):
        if 0 + s + 1 <= times[0]:
            need = False
            break
        if times[i + 1] - times[i] >= 2 + 2 * s:
            result = times[i] + 1 + s
            break

    if result == 0 and need:
        result = times[n - 1] + 1 + s

    hour = result // 60
    minute = result % 60

    # print(hour, minute)
    pass
if __name__ == "__main__":
    main(10)