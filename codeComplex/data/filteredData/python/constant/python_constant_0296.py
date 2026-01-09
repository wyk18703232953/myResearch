def main(n):
    # Interpret n as the number of participants; keep other parameters fixed and deterministic.
    # Original input: k, n, s, p
    k = 3      # number of groups
    s = 5      # sheets needed per participant
    p = 10     # sheets per pack

    sheets = (n + s - 1) // s
    result = (sheets * k + p - 1) // p
    # print(result)
    pass
if __name__ == "__main__":
    main(100)