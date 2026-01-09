def main(n):
    # Generate deterministic input array of length n
    # Example: a[i] = i - n//2 to have both negative and non-negative numbers
    a = [i - n // 2 for i in range(n)]

    # Core logic from original program
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1

    if n % 2 == 1:
        i = a.index(min(a))
        a[i] = -a[i] - 1

    a_str = list(map(str, a))
    # print(" ".join(a_str))
    pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)