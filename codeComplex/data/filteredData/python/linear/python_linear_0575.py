import random

def solve(n, k):
    print(1 * k, end=' ')
    if n == 2:
        print(2 * k, end=' ')
    if n == 3:
        print(k, 3 * k, end=' ')
    else:
        temp = n // 2
        if n % 2 == 0:
            temp -= 1
        print((str(k) + ' ') * temp, end='')
        if n > 3:
            solve(n // 2, k * 2)

def main(n):
    # 生成测试数据，这里仅以 n 为规模参数，不需要额外输入
    # 如需使用随机测试，可在此基于 n 生成更多参数
    solve(n, 1)

if __name__ == "__main__":
    # 示例：使用固定规模 n 进行测试
    test_n = 10  # 可根据需要修改或在外部调用 main(n)
    main(test_n)