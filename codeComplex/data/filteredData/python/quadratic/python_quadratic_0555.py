def main(n):
    # 将 n 视为行列规模：n 行 n 列
    rows = n
    cols = n
    res = []
    for j in range(rows // 2):
        for k in range(cols):
            res.append(str(j + 1) + " " + str(k + 1))
            res.append(str(rows - j) + " " + str(cols - k))
    if rows % 2:
        for j in range(cols // 2):
            res.append(f"{rows // 2 + 1} {j + 1}")
            res.append(f"{rows // 2 + 1} {cols - j}")
        if cols % 2:
            res.append(f"{rows // 2 + 1} {cols // 2 + 1}")
    print("\n".join(res))


if __name__ == "__main__":
    main(5)