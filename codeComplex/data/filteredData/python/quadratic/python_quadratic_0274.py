import math

def main(n):
    # n 表示每个列表的长度
    if n <= 0:
        return
    # 构造两个长度为 n 的整数列表 x 和 y
    # x: 1, 2, ..., n
    x = [i for i in range(1, n + 1)]
    # y: 从 k 开始的连续整数，制造部分交集
    # 这里取 k = n // 2，保证有交集且确定性
    start = max(1, n // 2)
    y = [start + i for i in range(n)]

    xx = set(x)
    yy = set(y)
    common = xx.intersection(yy)
    output = []
    for i in x:
        if i in common:
            output.append(str(i))
    if output:
        # print(" ".join(output))
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)