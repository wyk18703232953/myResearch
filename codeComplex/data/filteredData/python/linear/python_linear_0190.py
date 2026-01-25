def main(n):
    # Generate deterministic input array A of size n
    # Example: A[i] = i + 1 for i in range(n)
    if n <= 0:
        return
    A = [i + 1 for i in range(n)]

    # Prefix sum array.
    prefix = [0] * n
    prefix[0] = A[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + A[i]

    # Binary Search.
    target = (sum(A) + 1) // 2

    for i in range(n):
        if prefix[i] < target:
            continue
        else:
            print(i + 1)
            break


if __name__ == "__main__":
    main(10)