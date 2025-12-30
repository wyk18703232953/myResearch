from random import randint

def main(n):
    # 生成一个 n x n 的随机网格，包含 '.' 和 '#'
    m = n
    arr = [["." for _ in range(m)] for _ in range(n)]
    arr2 = []

    # 根据 n 构造测试数据：随机填充 '#' 和 '.'
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append("#" if randint(0, 1) == 1 else ".")
        arr2.append(row)

    # 原逻辑：根据 arr2 计算 arr
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (
                arr2[i + 1][j] == "#" and
                arr2[i][j + 1] == "#" and
                arr2[i + 1][j + 1] == "#" and
                arr2[i - 1][j] == "#" and
                arr2[i][j - 1] == "#" and
                arr2[i - 1][j - 1] == "#" and
                arr2[i + 1][j - 1] == "#" and
                arr2[i - 1][j + 1] == "#"
            ):
                arr[i + 1][j] = "#"
                arr[i][j + 1] = "#"
                arr[i + 1][j + 1] = "#"
                arr[i - 1][j] = "#"
                arr[i][j - 1] = "#"
                arr[i - 1][j - 1] = "#"
                arr[i + 1][j - 1] = "#"
                arr[i - 1][j + 1] = "#"

    if arr == arr2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5) 进行一次运行
    main(5)