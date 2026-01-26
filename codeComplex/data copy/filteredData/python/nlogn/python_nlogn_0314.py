def main(n):
    # n as array length
    arr = [(i * 2 + 3) % (n + 7) for i in range(n)]
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
    main(10)