def main(n):
    # Interpret n as the length of the array; choose a fixed m derived from n
    m = n // 2

    # Deterministically generate the array:
    # Values cycle around m using a simple pattern ensuring presence of <, =, > m
    arr = [(i % 3) - 1 + m for i in range(n)]

    ma = {0: 1}
    s, fla, ans = 0, False, 0

    for v in arr:
        if v == m:
            fla = True
        elif v < m:
            s -= 1
        elif v > m:
            s += 1
        if fla:
            ans += ma.get(s, 0) + ma.get(s - 1, 0)

        else:
            ma[s] = ma.get(s, 0) + 1

    # Keep the output to preserve core behavior
    # print(ans)
    pass
if __name__ == "__main__":
    # Example call with a chosen scale; adjust as needed for experiments
    main(10)