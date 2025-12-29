import random

def main(n: int):
    # 根据规模 n 生成一个测试输入值 x（保证 x >= 10 以便 4 和 9 的分解合理）
    if n < 10:
        x = 10
    else:
        # 在 [10, n] 范围内随机取一个整数作为测试数据
        x = random.randint(10, n)

    # 原始逻辑：对 x 进行分解
    if x % 2 == 0:
        a, b = 4, x - 4
    else:
        a, b = 9, x - 9

    # 返回结果而不是直接打印，方便在外部使用或测试
    return x, a, b

# 示例：如需直接运行测试，可取消下面注释
# if __name__ == "__main__":
#     x, a, b = main(100)
#     print("x =", x)
#     print(a, b)