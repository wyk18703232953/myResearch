def main(n):
    # 解释输入结构：
    # 原程序：
    # n = int(input())           # 一个整数（规模）
    # m = input().split(' ')     # 长度为 n 的整数序列（以空格分隔）
    #
    # 因此这里将 n 视为序列长度，构造一个确定性的整数列表 m。
    #
    # 构造规则（确定性且规模可控）：
    # m[i] = i % 5  （0,1,2,3,4 循环）
    #
    # 这样 m 的长度等于 n，适合作为时间复杂度实验的规模参数。
    m = [i % 5 for i in range(n)]

    mark = [1]
    j = 0
    for i in range(1, len(m)):
        tmp = max(mark[i - 1], m[i] + 1)
        mark.append(tmp)

    j += mark[len(m) - 1] - m[len(m) - 1] - 1
    for i in range(len(m) - 2, -1, -1):
        if mark[i] < mark[i + 1] - 1:
            mark[i] = mark[i + 1] - 1
        j += mark[i] - m[i] - 1

    print(j)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值做规模实验
    main(10)