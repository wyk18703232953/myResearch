def main(n):
    # 解释输入结构：
    # 原程序从一行读取两个整数 a, b
    # 在这里，我们用 n 决定 a 的规模，b 为与 a 同阶的确定性函数
    # 设定：
    #   a = n + 1  (保证 a >= 1，当 n=0 时 a=1)
    #   b = n // 2
    a = n + 1
    b = n // 2

    if b >= a - 1:
        result = a - 1
    else:
        summ = b
        k = a - b
        for i in range(2, k + 1):
            summ += i
        result = summ

    print(result)


if __name__ == "__main__":
    # 示例调用，可以根据需要修改 n 的值进行规模化实验
    main(10)