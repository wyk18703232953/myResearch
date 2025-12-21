def main(n):
    nums = list(range(1, n + 1))
    if n > 1:
        nums[0], nums[-1] = nums[-1], nums[0]
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
        return "Um_nik"
    else:
        return "Petr"

if __name__ == "__main__":
    print(main(10))