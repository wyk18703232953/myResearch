def main(n):
    # 确定性生成 k，使得存在解
    # 这里构造 k 为 c=1 时的值：k = 1*(1+1)//2 - (n-1) = 2 - n
    k = 2 - n

    c = 1
    while c * (c + 1) // 2 < k:
        c += 1
    while c * (c + 1) // 2 - (n - c) != k:
        c += 1
    print(n - c)


if __name__ == "__main__":
    # 示例：使用一个确定性的 n 调用
    main(1000)