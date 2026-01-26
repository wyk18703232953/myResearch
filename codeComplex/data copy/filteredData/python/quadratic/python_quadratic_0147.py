def main(n):
    c = [0] * 4
    # 生成 4 个 n 行 n 列的确定性 01 字符串矩阵作为原来的 4 组输入
    # 使用简单算术构造：第 k 组第 i 行第 j 列为 ((i + j + k) % 2)
    for k in range(4):
        for i in range(n):
            s = ''.join(str((i + j + k) % 2) for j in range(n))
            for j in range(n):
                if (i + j) % 2 != int(s[j]):
                    c[k] += 1
    c.sort()
    result = c[0] + c[1] + 2 * n * n - c[2] - c[3]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)