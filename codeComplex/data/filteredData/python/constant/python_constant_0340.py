import random

def main(n):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为测试数据
    # 若需要批量测试，可自行扩展为生成多个随机数列表等
    if n == 0:
        print(0)
    else:
        if n % 2 == 0:
            print(n + 1)
        else:
            print((n + 1) // 2)

# 示例：如需测试，可调用 main：
# main(10)