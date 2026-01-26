def main(n):
    # 由 n 确定性生成 m，这里令 m = n 的平方
    m = n * n
    result = m % (2 ** n if n >= 0 else 1)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)