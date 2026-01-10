def main(n):
    # n 不直接参与算法，仅用于构造确定性数据
    # 将坐标规模与 n 关联，使得可规模化
    queen_x = n
    queen_y = 2 * n
    king_x = 0
    king_y = n
    tar_x = 2 * n
    tar_y = 3 * n

    min_x, max_x = sorted([king_x, tar_x])
    min_y, max_y = sorted([king_y, tar_y])

    if max_x > queen_x > min_x or max_y > queen_y > min_y:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main(10)