def main(n):
    # 映射：原程序中 n, m 分别为元素种类数和元素总数
    # 这里设定 m = n * 2，构造一个长度为 m 的列表 c
    # c 中的值在 1..n 之间循环出现，保证可重复且确定性
    m = n * 2
    c = [str((i % n) + 1) for i in range(m)]
    col = [0] * n
    for i in range(len(c)):
        col[int(c[i]) - 1] += 1
    result = min(col)
    return result

if __name__ == "__main__":
    # 示例调用
    # print(main(10))
    pass