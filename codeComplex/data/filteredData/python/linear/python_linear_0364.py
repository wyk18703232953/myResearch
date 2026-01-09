def main(n):
    # Interpret n as the length of arrays a and b
    m = n

    # Deterministic data generation for a and b
    # Example: a is increasing, b is every second integer
    a = [i for i in range(1, n + 1)]
    b = [i * 2 for i in range(1, m + 1)]

    ans = 0
    for i in range(len(a)):
        if len(b) == 0:
            break
        if b[0] >= a[i]:
            ans += 1
            del b[0]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)