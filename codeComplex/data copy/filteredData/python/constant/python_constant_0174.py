def main(n):
    # Interpret n as a bound to deterministically generate l and r
    # Ensure r > l to mimic a valid interval
    l = n // 2
    r = l + (n % 5) + 1

    if l % 2 == 0 and r - l > 1:
        # print(l, l + 1, l + 2, end=" ")
        pass
    elif l % 2 != 0 and r - l > 2:
        # print(l + 1, l + 2, l + 3, end=" ")
        pass

    else:
        # print("-1")
        pass
if __name__ == "__main__":
    main(10)