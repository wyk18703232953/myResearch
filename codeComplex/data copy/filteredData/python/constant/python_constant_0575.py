def main(n):
    # 确定性生成输入数据
    # 将 x, y 映射到棋盘内的某个位置
    if n <= 0:
        return
    x = n // 2 + 1 if n >= 2 else 1
    y = n // 3 + 1 if n >= 3 else 1
    x = min(x, n)
    y = min(y, n)

    if max(x - 1, y - 1) > max(n - x, n - y):
        # print("Black")
        pass

    else:
        # print("White")
        pass
if __name__ == "__main__":
    main(8)