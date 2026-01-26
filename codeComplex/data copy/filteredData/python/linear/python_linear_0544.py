def main(n):
    if n <= 0:
        return
    if n == 1:
        # 单字符串输入情形：生成长度为 n 的确定性字符串
        a = "a" * n
        # print(a)
        pass

    else:
        # 原始程序中：n 表示列表长度
        # 生成一个长度为 n 的确定性整数列表，包含正负数和零的模式
        a = [(-1) ** i * i for i in range(1, n + 1)]
        b = [abs(i) for i in a]
        if min(a) * max(a) > 0:
            # print(sum(b) - 2 * min(b))
            pass

        else:
            # print(sum(b))
            pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    main(5)