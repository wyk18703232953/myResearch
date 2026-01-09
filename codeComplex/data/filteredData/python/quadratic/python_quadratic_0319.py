def main(n):
    # Interpret n as the length of the list
    m = max(1, n // 2)
    lst = [(i * 3 + 1) % 1000 for i in range(n)]

    arr = [0.0] * (n + 1)
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += lst[j]
            length = j - i + 1
            avg = summ / length
            idx = j - i
            if avg > arr[idx]:
                arr[idx] = avg
    if m - 1 < len(arr):
        result = max(arr[m - 1:])

    else:
        result = 0.0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)