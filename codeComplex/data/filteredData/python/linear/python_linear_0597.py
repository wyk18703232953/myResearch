def main(n):
    if n < 4:
        # print(0)
        pass
        return
    rang = list(range(2, n // 2 + 1))
    a = [i * (n // i - 1) for i in rang]
    # print(sum(a) * 4)
    pass
if __name__ == "__main__":
    # 示例：以 n = 100 作为输入规模进行一次确定性实验
    main(100)