def main(n):
    # 设定矩阵规模：n 行，m 列，这里令 m = n 保持规模一致
    if n <= 0:
        return
    m = n

    # 构造一个 n x m 的矩阵，全部为 'W'
    li = [['W' for _ in range(m)] for _ in range(n)]

    # 在中间区域放置一个连续的 'B' 方块，大小约为 n//2
    # 这样可以保证随 n 增大，有可扫描的 B 区域
    block_size = max(1, n // 2)
    top = (n - block_size) // 2
    left = (m - block_size) // 2
    for i in range(top, top + block_size):
        for j in range(left, left + block_size):
            li[i][j] = 'B'

    # 以下为原算法逻辑，只是移除了输入，直接在 li 上运行
    for j in range(m):
        flag = False
        for i in range(n):
            if li[i][j] == "B":
                flag = True
                position1 = i
                break
        if flag:
            break

    for j in range(m - 1, -1, -1):
        flag = False
        for i in range(n - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position2 = i
                break
        if flag:
            break

    for i in range(n):
        flag = False
        for j in range(m):
            if li[i][j] == "B":
                flag = True
                position3 = j
                break
        if flag:
            break

    for i in range(n - 1, -1, -1):
        flag = False
        for j in range(m - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position4 = j
                break
        if flag:
            break

    avg1 = (position1 + position2) // 2 + 1
    avg2 = (position3 + position4) // 2 + 1
    print(avg1, avg2)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行规模实验
    main(10)