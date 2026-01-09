def main(n):
    if n <= 0:
        return

    # 确定性生成 left 和 right
    left = [i % 3 for i in range(n)]
    right = [(n - 1 - i) % 3 for i in range(n)]

    rank = [x + y for (x, y) in zip(left, right)]
    arr = [n - r for r in rank]

    # check left
    for i in range(n):
        more = 0
        for j in range(i):
            if arr[j] > arr[i]:
                more += 1
        if more != left[i]:
            # print('NO')
            pass
            return

    # check right
    for i in range(n):
        more = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                more += 1
        if more != right[i]:
            # print('NO')
            pass
            return

    # print('YES')
    pass
    for x in arr:
        # print(x, end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)