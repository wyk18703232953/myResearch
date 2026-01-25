def main(n):
    from math import sqrt

    if n <= 0:
        return

    r = max(1, n // 2)

    x = [i * 3 for i in range(n)]

    arr = []
    for i in range(n):
        arr.append(r)
        for j in range(i):
            dx = x[j] - x[i]
            if abs(dx) <= (r * 2):
                val = arr[j] + sqrt((r * r * 4) - (dx * dx))
                if val > arr[i]:
                    arr[i] = val

    arr1 = [str(v) for v in arr]
    print(" ".join(arr1))


if __name__ == "__main__":
    main(10)