def main(n):
    # Generate deterministic input of size n
    # Original input: first line n, second line n integers
    # Here we generate a non-decreasing list with possible duplicates
    a = [i // 2 for i in range(n)]

    a.sort()
    t = 0
    for i in range(1, n):
        t += a[i] == a[i - 1]
    if t >= 2:
        return "cslnb"
    if t:
        for i in range(n):
            if a[i] == a[i + 1]:
                if a[i] and a[i] != a[i - 1] + 1:
                    a[i] -= 1
                    break

                else:
                    return "cslnb"
    return ["cslnb", "sjfnb"][(sum(a) - t - n * (n - 1) // 2) & 1]


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    result = main(10)
    # print(result)
    pass