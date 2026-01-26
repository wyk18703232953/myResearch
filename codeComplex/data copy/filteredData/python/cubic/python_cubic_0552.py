def main(n):
    # Deterministic generation of input data from n
    # String of digits '1' .. determined by n, length = max(1, n)
    length = max(1, n)
    mass = [str((i % 10)) for i in range(1, length + 1)]
    # Threshold b grows with n to keep algorithm meaningful
    b = int("".join(sorted(mass, reverse=True))) if mass else 0

    # Core algorithm (unchanged logic)
    mass.sort()
    mass = mass[::-1]
    p = ''
    while len(mass) > 0:
        for i in range(len(mass)):
            candidate = p + mass[i] + ''.join(sorted(mass[:i] + mass[i + 1:]))
            if int(candidate) <= b:
                p += mass[i]
                mass = mass[:i] + mass[i + 1:]
                break

        else:
            # If no digit can be chosen without exceeding b, terminate
            break

    # print(p)
    pass
if __name__ == "__main__":
    # Example call for time-complexity experiments
    main(10)