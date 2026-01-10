def main(n):
    segments = []

    # 确定性生成 n 个线段 (a, b)
    # 规则：a = i, b = i + (i % 3) + 1，确保 b > a 且可产生重叠
    for i in range(1, n + 1):
        a = i
        b = i + (i % 3) + 1
        segments.append(((a, b), i))

    segments.sort(key=lambda x: (x[0][0], -x[0][1]))

    last_r = 0
    last_index = 0

    for segment, index in segments:
        if last_r >= segment[1]:
            print(index, last_index)
            break

        last_r = segment[1]
        last_index = index
    else:
        print(-1, -1)


if __name__ == "__main__":
    # 示例规模，可以按需修改或在外部多次调用 main(n)
    main(10)