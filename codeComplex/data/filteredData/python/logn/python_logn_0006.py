def main(n):
    # Interpret n as the magnitude of the interval length.
    # We deterministically construct l and r based on n.
    # Ensure l < r and they differ so the algorithm does meaningful work.
    l = n
    r = n * 2 + 1

    target, final = l ^ r, 1
    while target:
        target >>= 1
        final <<= 1
    result = final - 1
    # print(result)
    pass
    return result

if __name__ == "__main__":
    # Example deterministic call
    main(10)