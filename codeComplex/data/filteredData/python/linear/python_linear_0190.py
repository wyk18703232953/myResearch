def main(n):
    # Deterministically generate input array A of size n
    A = [(i % 10) + 1 for i in range(n)]

    # Prefix sum array.
    prefix = [0] * n
    prefix[0] = A[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + A[i]

    # Binary Search target.
    target = (sum(A) + 1) // 2

    # Find and return the position (1-based) instead of printing
    for i in range(n):
        if prefix[i] < target:
            continue

        else:
            return i + 1
    return -1  # In case no index satisfies the condition


if __name__ == "__main__":
    # Example deterministic call for experimentation
    result = main(10)
    # print(result)
    pass