def main(n):
    # 生成确定性的输入数据：n 对 (a, b)
    # 映射：第 i 对为 (i % 10, i // 2)，并记录原始下标 i
    pairs = [[i % 10, i // 2, i] for i in range(n)]

    # 原逻辑：按 (a 升序, b 降序) 排序
    pairs.sort(key=lambda x: (x[0], -x[1]))

    # 查找满足条件的第一对
    for i in range(1, n):
        if pairs[i][1] <= pairs[i - 1][1]:
            # print(pairs[i][2] + 1, pairs[i - 1][2] + 1)
            pass
            break

    else:
        # print(-1, -1)
        pass
if __name__ == "__main__":
    # 示例：可按需修改 n 进行规模化实验
    main(10)