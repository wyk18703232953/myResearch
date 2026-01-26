def main(n):
    # Interpret n as the number of intervals
    # Deterministically generate t and interval data based on n
    t = (n % 5) + 1  # small positive float/integer gap threshold

    cont = []
    # Generate n intervals deterministically
    # Center increases with i, length varies in a simple deterministic pattern
    for i in range(n):
        hcenter = float(i * 3)  # centers spaced by 3 units
        hlen = float((i % 4) + 1)  # lengths cycle through 1,2,3,4
        cont.append([hcenter - hlen / 2.0, hcenter + hlen / 2.0])

    ans = 2
    cont.sort(key=lambda it: it[0])
    for i in range(n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap > t:
            ans += 2
        elif gap == t:
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)