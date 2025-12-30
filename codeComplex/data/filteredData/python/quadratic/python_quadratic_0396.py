def main(n: int):
    # 生成测试数据：n 行，每行长度为 2*n-1，构造一段连续的 'B'
    # 行索引 i0，列索引 j0 为起始 'B' 的位置，长度为 L
    # 满足 (L // 2) + 1 仍在边界内，以保证与原逻辑兼容
    if n <= 0:
        return

    # 简单选择：i0 为中间行，j0 为 0，长度 L 为奇数且不超过 (2*n-1)
    i0 = n // 2
    L = min(2 * (n // 2) + 1, 2 * n - 1)  # 确保 L 为奇数且合规
    j0 = 0
    width = 2 * n - 1  # 每行长度

    for i in range(n):
        if i == i0:
            # 构造包含连续 'B' 的一行
            line = ['.'] * width
            for k in range(L):
                line[j0 + k] = 'B'
            mat = ''.join(line)
        else:
            # 其他行不含 'B'
            mat = '.' * width

        # 原始逻辑应用在当前行上（模拟逐行输入）
        # 只有第一次遇到含 'B' 的行才会触发输出
        if 'B' in mat:
            j = mat.find('B')
            c = mat.count('B') // 2 + 1
            i_res = i + c
            j_res = j + c
            print(i_res, j_res)
            break


if __name__ == "__main__":
    # 示例调用，规模为 5（可根据需要修改或在外部调用 main）
    main(5)