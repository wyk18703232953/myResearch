def main(n):
    # Deterministically generate k based on n, ensure k >= 1 to avoid division by zero
    k = n + 1
    result = (2 * n + k - 1) // k + (5 * n + k - 1) // k + (8 * n + k - 1) // k
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call
    main(10)