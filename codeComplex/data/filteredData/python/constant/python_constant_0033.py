import random

def main(n: int):
    """
    n 为规模参数，这里用于控制测试数据数量或上限。
    根据 n 生成一个测试整数 x（1 到 n 之间），
    然后对原逻辑进行计算并返回结果。
    """
    if n <= 0:
        return 0

    # 根据规模 n 生成测试数据：随机整数 x ∈ [1, n]
    x = random.randint(1, n)

    # 原始逻辑：对输入 x 进行计算
    num = x + x // 2

    # 此处选择返回结果；如需打印可改为 print(num)
    return num

# 示例：自行测试时可取消下面注释
# if __name__ == '__main__':
#     result = main(10)
#     print(result)