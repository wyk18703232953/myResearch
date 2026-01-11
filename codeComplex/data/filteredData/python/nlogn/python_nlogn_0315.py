def main(n):
    # n: size of the array
    if n <= 0:
        return

    # Deterministic data generation
    # Example: decreasing sequence with some variation
    arr = [(n - i) + (i % 3) for i in range(n)]

    gap = n // 2
    count = 0
    while gap >= 1:
        for j in range(gap, n):
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break

                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                    count += 1
                i -= gap
        gap //= 2

    if count % 2 == 3 * n % 2:
        # print("Petr")
        pass

    else:
        # print("Um_nik")
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)