def main(n):
    # 生成确定性输入数据：列表长度为 n，元素值有重复，以便 index(c) 能找到
    a = [i // 2 for i in range(n)]
    ans = 0
    # 使用与原程序等价的逻辑
    while len(a) > 0:
        c = a.pop(0)
        # 原代码假设一定能找到 c，这里保持这个假设
        i = a.index(c)
        ans += i
        del a[i]
    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)