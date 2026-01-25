def main(n):
    # Ensure n is positive
    if n <= 0:
        print("NO")
        return

    # Deterministic generation of left and right based on n
    # Example pattern:
    # left[i] = i % 3
    # right[i] = (n - 1 - i) % 3
    left = [(i % 3) for i in range(n)]
    right = [((n - 1 - i) % 3) for i in range(n)]

    rank = [x + y for (x, y) in zip(left, right)]
    arr = [(n - r) for r in rank]

    # check left
    for i in range(n):
        more = 0
        for j in range(i):
            if arr[j] > arr[i]:
                more += 1
        if more != left[i]:
            print('NO')
            return

    # check right
    for i in range(n):
        more = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                more += 1
        if more != right[i]:
            print('NO')
            return

    print('YES')
    for x in arr:
        print(x, end=' ')
    print()


if __name__ == "__main__":
    # Example deterministic call; adjust n for experiments
    main(10)