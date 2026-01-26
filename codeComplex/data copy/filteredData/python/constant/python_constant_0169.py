def main(n):
    # Deterministic input generation based on n
    # We map n to l and r so that the core logic is exercised for various ranges.
    # Ensure l < r and range size varies with n.
    if n < 3:
        l = 1
        r = n + 1

    else:
        l = n
        r = 2 * n

    # Original core logic (refactored without input/exit)
    if r - l + 1 < 3:
        # print(-1)
        pass
        return

    if l % 2 == 0:
        # print(l, l + 1, l + 2)
        pass
        return

    if r - l + 1 > 3:
        # print(l + 1, l + 2, l + 3)
        pass
        return

    # print(-1)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimental purposes
    main(10)