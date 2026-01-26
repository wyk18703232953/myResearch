def main(n):
    # 将原本的两个输入整数 a, b 映射为确定性的函数
    # 这里令 a = n, b = n+1（b 不参与后续逻辑，仅保持结构）
    a = n
    b = n + 1

    q, r = divmod(a, 2)
    result = '01' * q + '0' * r
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值进行实验
    main(10)