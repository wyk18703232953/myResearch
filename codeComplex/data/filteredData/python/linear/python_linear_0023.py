def main(n):
    # Generate deterministic data: a list of n integers
    # Pattern: i % 3 to produce varied parity
    l = [i % 3 for i in range(n)]
    # Original logic: take numbers mod 2
    l_mod2 = [x % 2 for x in l]
    # Find index (1-based) where exactly one element is odd (if exists)
    has_single_odd = (sum(l_mod2) == 1)
    try:
        result = l_mod2.index(has_single_odd) + 1
    except ValueError:
        # If condition not satisfied, mimic behavior by returning 0
        result = 0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)