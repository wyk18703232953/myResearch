import math

def main(n):
    # 将 n 映射为原程序中的 m 和 n（这里统一用 m_dim, n_dim 避免名称冲突）
    # 约定：m_dim = n，n_dim = n，用于规模实验时同时放大两个维度
    m_dim = max(1, n)
    n_dim = max(1, n)

    result = []

    for column in range(1, math.ceil(m_dim / 2) + 1):
        rowRange = range(1, n_dim + 1)
        if column == math.ceil(m_dim / 2) and m_dim % 2 == 1:
            rowRange = range(1, math.ceil(n_dim / 2) + 1)

        for row in rowRange:
            result.append(str(column) + ' ' + str(row))
            if (
                row == math.ceil(n_dim / 2)
                and n_dim % 2 == 1
                and column == math.ceil(m_dim / 2)
                and m_dim % 2 == 1
            ):
                continue
            result.append(str(m_dim + 1 - column) + ' ' + str(n_dim + 1 - row))

    print('\n'.join(result))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 来进行规模实验
    main(5)