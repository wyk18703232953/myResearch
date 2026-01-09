def main(n):
    # In the original code, two integers n, m are read, but only n is used.
    # For scalability, we map the input scale parameter n to the original n,
    # and choose a deterministic m based on n (though unused by the logic).
    original_n = n
    m = n + 1  # deterministic, unused in logic

    # Core algorithm from original program
    out1 = (original_n - 1) * '4' + '5'
    out2 = original_n * '5'

    # print(out1)
    pass
    # print(out2)
    pass
if __name__ == "__main__":
    main(5)