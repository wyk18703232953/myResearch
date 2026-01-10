def main(n):
    # Deterministically generate nums as a permutation of [1..n]
    # Example: a simple rotation by 1 position
    nums = [((i + 1) % n) + 1 for i in range(n)]

    swaps = 0
    visited = set()
    for index in range(n):
        if index in visited:
            continue
        else:
            visited.add(index)
            length = 0
            value = nums[index]
            while value != index + 1:
                visited.add(value - 1)
                value = nums[value - 1]
                length += 1
            swaps += length

    if (3 * n - swaps) % 2:
        print("Um_nik")
    else:
        print("Petr")


if __name__ == "__main__":
    main(10)