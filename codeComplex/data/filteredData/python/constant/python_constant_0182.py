def main(n):
    # Map n to l and r deterministically
    l = n
    r = n + (n % 5)  # r - l in [0..4], deterministic mapping

    if r == l + 1 or r == l:
        result = -1
    elif l % 2 == 0:
        result = (l, l + 1, l + 2)
    elif abs(r - l) >= 3:
        result = (l + 1, l + 2, l + 3)

    else:
        result = -1

    # print(result)
    pass
if __name__ == "__main__":
    main(10)