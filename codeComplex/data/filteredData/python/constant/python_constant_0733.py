def main(n):
    # 原代码中 k 为输入的第一个数，这里用 n 来作为测试规模直接代替 k
    k = n

    a = []
    for i in range(0, 12):
        s = 9 * pow(10, i) * (i + 1)
        if k <= s:
            break

        else:
            k -= s
    pos = i + 1
    num = (pow(10, pos - 1) + (k // pos) - 1)
    if k % pos == 0:
        # print(str(num)[-1])
        pass

    else:
        # print(str(num + (0 if pos == 1 else 1))[(k % pos) - 1])
        pass
if __name__ == "__main__":
    # 示例：使用 n = 100 作为测试规模
    main(100)