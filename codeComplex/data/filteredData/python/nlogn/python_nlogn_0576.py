import random

def f(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2]
    if n == 3:
        return [1, 1, 3]
    if n > 3:
        L = f(n // 2)
        for i in range(len(L)):
            L[i] *= 2
        return [1] * (n - n // 2) + L

def main(n):
    # 这里根据规模 n 生成测试数据，本题逻辑为对单个整数 n 处理
    # 若需更复杂的数据，可在此扩展生成逻辑
    test_n = n

    L = f(test_n)
    s = ''
    for i in L:
        s += str(i) + ' '
    print(s)

# 示例：调用 main(10) 进行测试
if __name__ == "__main__":
    main(10)