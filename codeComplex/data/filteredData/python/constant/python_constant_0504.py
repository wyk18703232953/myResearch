def main(n):
    t = n
    results = []

    for i in range(t):
        # Deterministically generate n, m, k based on i and overall scale n
        ni = i
        mi = n - i
        ki = n

        ni = abs(ni)
        mi = abs(mi)
        if max(ni, mi) > ki:
            results.append("-1")

        else:
            bad1 = ((ni + ki) % 2 == 1)
            bad2 = ((mi + ki) % 2 == 1)
            results.append(str(ki - bad1 - bad2))

    # Join results with newlines to mimic original multi-line output
    output = "\n".join(results)
    # print(output)
    pass
    return output

if __name__ == "__main__":
    main(10)