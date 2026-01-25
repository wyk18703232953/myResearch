def main(n):
    # 确定性地生成输入数据：一个长度为 n 的整数列表
    # 示例规则：data[i] = i + 1，保证包含丰富的因子关系
    data = [i + 1 for i in range(n)]

    data.sort()
    ans = [0] * n
    col = 0
    for i in range(n):
        if ans[i] == 0:
            col += 1
            ans[i] = 1
            d = data[i]
            for j in range(i + 1, n):
                if data[j] % d == 0:
                    ans[j] = 1
    print(col)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(10)