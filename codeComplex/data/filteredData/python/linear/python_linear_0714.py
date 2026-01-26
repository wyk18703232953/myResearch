def main(n):
    # Generate a deterministic list A of length n
    # Ensure values are large enough so divisions are meaningful
    A = [(i * 7 + 3) % (10 ** 6) + 1 for i in range(n)]

    k = 10 ** 10
    if n >= 3:
        for i in range(1, n - 1):
            k = min(k, min(A[0], A[i]) // i)
            k = min(k, min(A[-1], A[i]) // (n - i - 1))
    if n >= 2:
        k = min(k, min(A[0], A[-1]) // (n - 1))
    # print(k)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)