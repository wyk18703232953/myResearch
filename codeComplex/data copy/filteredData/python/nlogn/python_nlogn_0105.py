def main(n):
    # 生成确定性的长度为 n 的数组
    # 示例：arr[i] = (i * 3 + 1) % (n + 5)
    arr = [(i * 3 + 1) % (n + 5) for i in range(n)]

    new = sorted(arr)
    count = 0

    for i in range(n):
        if arr[i] != new[i]:
            count += 1

    if count <= 2:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)