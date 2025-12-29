import random

def main(n: int):
    # 根据规模 n 生成一个不大于 n 的斐波那契数作为测试数据
    # 生成斐波那契序列，直到超过 n
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    # 去掉第一个超出 n 的数
    fib = [x for x in fib if x <= n]

    # 随机选择一个斐波那契数作为本次测试的输入 n_value
    n_value = random.choice(fib) if fib else 0

    # 下面是原逻辑的无 input() 版本，对 n_value 进行处理
    if n_value == 0:
        print(0, 0, 0)
    else:
        a, b = 0, 1
        while a + b != n_value:
            a, b = b, a + b
        print(0, a, b)

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)