import math
import random

def main(n: int):
    # 生成测试数据：
    # 将 types_of_toy 设为 n
    types_of_toy = n
    # toy_pair 在合法范围 [1, 2 * types_of_toy + n] 内随机生成，保证有越界情况
    toy_pair = random.randint(1, 2 * types_of_toy + n)

    # 原逻辑
    if toy_pair <= types_of_toy:
        result = math.floor((toy_pair - 1) / 2)
    elif toy_pair <= 2 * types_of_toy - 1:
        result = math.floor((types_of_toy + 1 - (toy_pair - types_of_toy)) / 2)
    else:
        result = 0

    print(result)


if __name__ == "__main__":
    # 示例：规模 n 可按需修改
    main(10)