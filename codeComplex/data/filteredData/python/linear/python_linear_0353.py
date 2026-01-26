def main(n):
    # 将原本的两个输入参数 n, m 映射为：字符串长度为 n，m 为占位参数
    # 生成一个确定性的 m（虽然原代码未使用，但保留结构）
    m = n + 1

    c = 0
    ans = str()
    for _ in range(n):
        ans += str(c ^ 1)
        c = c ^ 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行实验
    main(10)