def main(n):
    # 由于原程序读入的是一个整数 t，然后使用 n = t - 1，
    # 这里保持同样的逻辑：将传入的 n 当作原来的输入 t。
    n = n - 1
    x, y = 1, 9
    while n > x * y:
        n, x, y = n - x * y, x + 1, y * 10
    a = str(10 ** (x - 1) + n // x)[n % x]
    # print(a)
    pass
if __name__ == "__main__":
    # 示例测试：根据规模 n 生成一个测试
    # 可以自行修改下面的 n_test 验证不同规模
    n_test = 100  # 这里假设规模 n，就是原程序要读入的整数
    main(n_test)