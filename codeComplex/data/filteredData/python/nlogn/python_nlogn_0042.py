def main(n):
    # Ensure n is at least 1
    if n <= 0:
        return

    # Deterministically generate an array of length n
    # Example: arr[i] = (i % 5) + 1, ensuring some variety but bounded values
    arr = [(i % 5) + 1 for i in range(n)]

    mx = max(arr)
    x = -1
    if mx == 1:
        x = 2
    else:
        x = 1

    # Remove one occurrence of mx
    arr.remove(mx)
    arr.append(x)
    arr.sort()

    # For scalability experiments, we avoid printing huge outputs by limiting print size
    # but we still execute full algorithm on full data.
    limit = 100
    if len(arr) <= limit:
        print(*arr)
    else:
        # Print only first and last few elements to keep output manageable
        head = arr[:limit // 2]
        tail = arr[-limit // 2:]
        print(*head, '...', *tail)


if __name__ == "__main__":
    # Example deterministic call; adjust n for experiments
    main(10)